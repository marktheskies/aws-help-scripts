# Delete Old Backup Recovery Points

It is considered best practice to remove all EBS snapshots older than a defined date consistently. Currently, there is no easy way within the AWS console to delete all AWS Backup service snapshots older than a specific date outside of AWS Backup-managed retention policies. This is problematic if you remove a backup plan with existing snapshots.

Use this script to solve this problem and automate the deletion of Backup-created EBS snapshots older than a specific date.

## Installation

To get started, clone the repo and install the dependencies with pip.

```bash
git clone UPDATEME!
cd UPDATEME!
pip install -r requirements.txt
```

## Usage

Simply invoke from your terminal, defining your configuration in environment variables.

```bash
VAULT_NAME="Default" CREATED_BEFORE="2019-09-01" python delete_old_recovery_points.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
