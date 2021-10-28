# Enable EBS Encryption By Default

A simple script designed to help your organisation meet CIS baseline compliance within your AWS
account. The script simply enables EBS encryption by default across all enabled regions.

## How to Use

**Step 1 -** Clone this repo to your local machine.

```bash
git clone https://github.com/marktheskies/enable-ebs-encryption-by-default
cd enable-ebs-encryption-by-default
```

**Step 2 (Option 1) -** Set your AWS access key ID and AWS secret access key.

```bash
export AWS_ACCESS_KEY_ID="your_aws_access_key_id"
export AWS_SECRET_ACCESS_KEY="your_aws_secret_access_key"
```

**Step 2 (Option 2) -** Select your pre-configured AWS profile.

```bash
export AWS_PROFILE="your_profile_name"
```

**Step 3 -** Configure and activate your virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 4 -** Run it!

```bash
python enable-ebs-encryption-by-default.py
```
