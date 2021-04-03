from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import json
import os
import time

import boto3
from dotenv import load_dotenv
import praw

from .constants import ENDPOINT_URL, MAIN_TABLE_NAME
from .utils import (
    compose_expression_attr_vals,
    compose_update_expression,
    copy_dict_partial,
)


if os.environ.get("PYTHON_ENV", "prod") == "dev":
    load_dotenv()
    dynamo_db = boto3.resource(
        "dynamodb",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id="secret",
        aws_secret_access_key="secret",
    )
else:
    dynamo_db = boto3.resource("dynamodb", region_name="eu-west-1")

client_id = os.environ["REDDIT_CLIENT_ID"]
client_secret = os.environ["REDDIT_CLIENT_SECRET"]
user_agent = "fullstack fomo"

reddit = praw.Reddit(
    client_id=client_id, client_secret=client_secret, user_agent=user_agent
)
print("Connected to DynamoDB and Reddit client")


def _get_subreddit_data(subreddit: str) -> dict:
    return [
        {
            "id": submission.id,
            "title": submission.title,
            "dataSource": "reddit",
            "score": submission.score,
            "longText": submission.selftext,
            "link": submission.shortlink,
            "numComments": submission.num_comments,
            "thumbnail": submission.url,
            "author": submission.author_fullname,
            "subreddit": submission.subreddit_name_prefixed,
        }
        for submission in reddit.subreddit(subreddit).hot(limit=5)
    ]


def main(event, context) -> None:
    start_time = time.time()

    reddit_table = dynamo_db.Table("FomoSubreddits")
    main_table = dynamo_db.Table(MAIN_TABLE_NAME)
    items = [
        item["subreddit"] for item in reddit_table.scan().get("Items", [])
    ]

    if not items:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Not tracking any subreddits"}),
        }

    print("Fetching latest reddit data...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        iterator = executor.map(_get_subreddit_data, items[:1])
    results = [item for result in iterator for item in result]

    print("Checking for updated data and updating main DynamoDB table.")
    now_time = datetime.utcnow().isoformat()
    for result in results:
        key = {"id": result["id"], "dataSource": result["dataSource"]}
        existing_item = main_table.get_item(Key=key).get("Item", False)

        if existing_item:
            print(
                f"Updating entry for item ID: {result['id']}, source: {result['dataSource']}"
            )
            updated_item = copy_dict_partial(
                result, exclude_keys=["id", "dataSource"]
            )
            updated_item["updatedAt"] = now_time
            main_table.update_item(
                Key=key,
                UpdateExpression=compose_update_expression(updated_item),
                ExpressionAttributeValues=compose_expression_attr_vals(
                    updated_item
                ),
            )
        else:
            print(
                f"Creating entry for item ID: {result['id']}, source: {result['dataSource']}"
            )
            result["createdAt"] = now_time
            result["updatedAt"] = now_time
            main_table.put_item(Item=result)

    delta_time = time.time() - start_time
    message = f"Function took {delta_time:.2f}secs to run"

    if os.environ.get("PYTHON_ENV", "prod") == "dev":
        return {"statusCode": 200, "body": json.dumps({"message": message})}
