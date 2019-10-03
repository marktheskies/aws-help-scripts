import datetime
import json
import os

import boto3


def delete_recovery_point(client: boto3.client, vault_name: str, arn: str) -> None:
    "Deletes a recovery point with the given arn from a given vault"
    client.delete_recovery_point(BackupVaultName=vault_name, RecoveryPointArn=arn)


def get_old_recovery_points(
    client: boto3.client, vault_name: str, created_before: datetime.datetime
) -> list:
    "Returns a list of ARNs for all recovery points in the given vault created before a given date"
    response = client.list_recovery_points_by_backup_vault(
        BackupVaultName=vault_name, ByCreatedBefore=created_before
    )

    return response["RecoveryPoints"]


if __name__ == "__main__":
    client = boto3.client("backup")

    created_before = datetime.datetime.strptime(
        os.environ["CREATED_BEFORE"], "%Y-%m-%d"
    )
    vault_name = os.environ["VAULT_NAME"]

    recovery_points = get_old_recovery_points(client, vault_name, created_before)

    for recovery_point in recovery_points:
        delete_recovery_point(client, vault_name, recovery_point["RecoveryPointArn"])
        print("Deleted {}".format(recovery_point["RecoveryPointArn"]))
