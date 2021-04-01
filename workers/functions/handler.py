import os
import json
from datetime import datetime


if os.environ.get("PYTHON_ENV", "prod") == "dev":
    from dotenv import load_dotenv


def yeet(event, context):
    body = {
        "message": "This is a test handler",
    }

    print("The function is running")
    print(body)
    now_str = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    print(f"Function finished running at {now_str}")

    if os.environ.get("PYTHON_ENV", "prod") == "dev":
        load_dotenv()
        return {"statusCode": 200, "body": json.dumps(body)}
