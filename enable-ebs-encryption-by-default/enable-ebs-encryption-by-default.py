import boto3

if __name__ == "__main__":

    ec2 = boto3.client("ec2")
    response = ec2.describe_regions()
    regions = response["Regions"]

    for region in regions:
        ec2 = boto3.client("ec2", region_name=region["RegionName"])
        ec2.enable_ebs_encryption_by_default()
        print(f'Enabled EBS encryption by default in {region["RegionName"]}')
