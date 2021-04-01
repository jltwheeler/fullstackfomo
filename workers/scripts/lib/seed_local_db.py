import boto3

import config as cfg


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
    existing_table_names = [table.name for table in existing_tables]
    print(existing_table_names)

    # Create tables and populate with seed data
    for table in cfg.FOMO_TABLES:
        if table["name"] not in existing_table_names:
            print(f"Creating table {table['name']}")
            dynamo_table = dynamo_db.create_table(
                TableName=table["name"],
                AttributeDefinitions=table["definitions"],
                KeySchema=table["key_schema"],
                ProvisionedThroughput=table["units"],
            )

            if table.get("file", False):
                print(f"Putting seed items into {table['name']}")
                data = cfg.get_data(table["file"])
                for item in data:
                    dynamo_table.put_item(Item=item)

                existing_tables.append(dynamo_table)


if __name__ == "__main__":
    main()