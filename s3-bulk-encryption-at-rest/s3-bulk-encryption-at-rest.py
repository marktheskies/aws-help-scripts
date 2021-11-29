import boto3
import botocore

if __name__ == "__main__":
    # Get a list of buckets from S3
    client = boto3.client("s3")
    response = client.list_buckets()
    buckets = response["Buckets"]

    for bucket in buckets:
        try:
            client.get_bucket_encryption(Bucket=bucket["Name"])
        # If we catch a ServerSideEncryptionConfigurationNotFoundError, the bucket doesn't have
        # default encryption at rest enabled. Confirm with the user and enable it.
        except botocore.exceptions.ClientError as error:
            if (
                error.response["Error"]["Code"]
                == "ServerSideEncryptionConfigurationNotFoundError"
            ):
                confirmation = input(
                    f'Enable at-rest encryption by default for {bucket["Name"]}? [Y/n]: '
                )
                if confirmation.upper() == "Y" or confirmation == "":
                    client.put_bucket_encryption(
                        Bucket=bucket["Name"],
                        ServerSideEncryptionConfiguration={
                            "Rules": [
                                {
                                    "ApplyServerSideEncryptionByDefault": {
                                        "SSEAlgorithm": "AES256"
                                    }
                                },
                            ]
                        },
                    )
            else:
                raise error
