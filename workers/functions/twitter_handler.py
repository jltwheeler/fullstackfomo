import os
import json
import time

import tweepy
from dotenv import load_dotenv


if os.environ.get("PYTHON_ENV", "prod") == "dev":
    load_dotenv()

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_num_replies(api: tweepy.API, user_name: str, since_id: int) -> int:
    replies = tweepy.Cursor(
        api.search,
        q=f"to:{user_name}",
        since_id=since_id,
        tweet_mode="extended",
    ).items()
    return sum(x.in_reply_to_status_id == since_id for x in replies)


def main(event, context) -> None:
    start_time = time.time()

    user_name = "wesbos"
    user_timeline = api.user_timeline(
        screen_name=user_name,
        exclude_replies=True,
        include_rts=True,
        since_id=None,
    )
    ids = user_timeline.ids()

    for tweet in user_timeline:
        # fomo_tweet = {
        #     hype: tweet.

        # }
        tweet.id
        replies = get_num_replies(
            api,
            user_name,
        )
        tweet.retweet_count
        tweet.text
        tweet.favorite_count

    print(count)
    delta_time = time.time() - start_time

    message = f"Function took {delta_time:.2f}secs to run"
    if os.environ.get("PYTHON_ENV", "prod") == "dev":
        load_dotenv()
        return {"statusCode": 200, "body": json.dumps({"message": message})}
