import os
import json
from decimal import Decimal

REGION_NAME = "eu-west-1"
FOMO_TABLES = [
    {
        "name": "FomoMain",
        "definitions": [
            {"AttributeName": "id", "AttributeType": "S"},
            {"AttributeName": "dataSource", "AttributeType": "S"},
        ],
        "key_schema": [
            {"AttributeName": "id", "KeyType": "HASH"},
            {"AttributeName": "dataSource", "KeyType": "RANGE"},
        ],
        "units": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
    },
    {
        "name": "FomoTwitterUsers",
        "definitions": [
            {"AttributeName": "userName", "AttributeType": "S"},
        ],
        "key_schema": [
            {"AttributeName": "userName", "KeyType": "HASH"},
        ],
        "units": {
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1,
        },
        "file": "twitter.json",
    },
    {
        "name": "FomoSubreddits",
        "definitions": [
            {"AttributeName": "subreddit", "AttributeType": "S"},
        ],
        "key_schema": [
            {"AttributeName": "subreddit", "KeyType": "HASH"},
        ],
        "units": {
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1,
        },
        "file": "reddit.json",
    },
]


def get_data(json_file: str) -> dict:
    with open(os.path.join(os.getcwd(), "data", json_file), "rb") as file:
        users = json.load(file, parse_float=Decimal)
    return users