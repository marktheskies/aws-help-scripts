# S3 Bulk Encryption at Rest

This script is designed to help you in the right direction to acheive CIS benchmark compliance within your AWS account by providing a simple way to enable AES-256 SSE by default on all buckets in your AWS account.

## Running the script

### Step 1 -

Clone this repo and enter the script directory.

```bash
git clone https://github.com/marktheskies/aws-helper-scripts.git
cd aws-helper-scripts/s3-bulk-encryption-at-rest
```

### Step 2 -

Create a Python virtual environment, activate it and install dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3 -

Run the Python script. For each bucket that has SSE _disabled_ by default, the script will prompt to enable it.

```bash
python s3-bulk-encryption-at-rest.py
```

Example output:

```
Enable at-rest encryption by default for your-important-bucket? [Y/n]:
```

## How to contribute

If you would like to contribute, please open an issue or create a PR with your proposed changes.

## Mentions

This architecture is based on guidelines defined in Section 2 (Storage) of CIS Amazon Web Services Foundations v1.4.0.
