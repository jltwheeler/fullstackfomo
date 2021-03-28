import os
import json
from datetime import datetime


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
    }

    print("The function is running")
    print(body)
    now_str = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    print(f"Function finished running at {now_str}")

    if os.environ.get("PYTHON_ENV", "prod") == "dev":
        return {"statusCode": 200, "body": json.dumps(body)}
