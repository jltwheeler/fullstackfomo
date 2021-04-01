import boto3


def main():
    ENDPOINT_URL = "http://localhost:8000"
    dynamo_db = boto3.resource(
        "dynamodb",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id="secret",
        aws_secret_access_key="secret",
        region_name="eu-west-1",
    )
    print(f"Connected to local dynamodb database on {ENDPOINT_URL}")

    existing_tables = list(dynamo_db.tables.all())
    for table in existing_tables:
        table.delete()
        print(f"Deleted {table.name}.")

    print(f"Finished dropping {len(existing_tables)} tables.")


if __name__ == "__main__":
    main()