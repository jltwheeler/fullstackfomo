import os
import time
import json
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
import praw
import boto3

from .constants import ENDPOINT_URL

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


def _get_subreddit_data(subreddit: str) -> dict:
    return [
        {
            "id": submission.id,
            "title": submission.title,
            "type": "reddit",
            "score": submission.score,
            "text": submission.selftext,
            "link": submission.permalink,
            "num_comments": submission.num_comments,
            "thumbnail": submission.url,
        }
        for submission in reddit.subreddit(subreddit).hot(limit=5)
    ]


def main(event, context) -> None:
    start_time = time.time()

    table = dynamo_db.Table("FomoSubreddits")
    items = [item["subreddit"] for item in table.scan().get("Items", [])]

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(_get_subreddit_data, items)

    output = [item for result in results for item in result]

    with open("test.json", "w") as f:
        json.dump(output, f, indent=2)

    delta_time = time.time() - start_time
    message = f"Function took {delta_time:.2f}secs to run"

    if os.environ.get("PYTHON_ENV", "prod") == "dev":
        load_dotenv()
        return {"statusCode": 200, "body": json.dumps({"message": message})}