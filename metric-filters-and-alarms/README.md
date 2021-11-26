# Metric Filters and Alarms

This architecture is designed to help you in the right direction to acheive CIS benchmark compliance within your AWS account by providing metric filters and alarms to a specified endpoint. For example, you can notify your security team via ticketing system.

## Important

The alarm for Console Signin Without MFA assumes that you enforce MFA at the IdP level. We use Google Workspaces at my current organisation and therefore cannot manage MFA within AWS SSO.

If you use an IdP offically supported by AWS SSO, or do not use AWS SSO, change ConsoleLoginWithoutMfaMetricFilter.Properties.FilterPattern as per below.

```yaml
ConsoleLoginWithoutMfaMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      FilterPattern: '{ ($.eventName = "ConsoleLogin") && ($.additionalEventData.MFAUsed != "Yes") }'
      ...
```

## How to deploy the architecture for the first time

If you are deploying this architecture for the first time, follow these steps.

### Step 1 -

Clone this repo and enter the script directory.

```bash
git clone https://github.com/marktheskies/aws-helper-scripts.git
cd aws-helper-scripts/metric-filters-and-alarms
```

### Step 2 -

Run the following AWS CLI command to deploy the CloudFormation stack containing the alarms and filters. Replace `<email_address_for_notifications>` and `<cloudtrail_cloudwatch_log_group>` as appropriate.

```bash
aws cloudformation create-stack --template-body file://metric-filters-and-alarms.cfn.yml --stack-name Metric-Filters-And-Alarms --parameters ParameterKey=NotificationEmailAddress,ParameterValue=<email_address_for_notifications> ParameterKey=CloudTrailLogGroup,ParameterValue=<cloudtrail_cloudwatch_log_group>
```

## How to update the architecture

If you have already deployed the architecture and are updating the stack, follow these steps.

### Step 1 -

Clone this repo and enter the script directory.

```bash
git clone https://github.com/marktheskies/aws-helper-scripts.git
cd aws-helper-scripts/metric-filters-and-alarms
```

### Step 2 -

Run the following AWS CLI command to update the CloudFormation stack. Replace `<email_address_for_notifications>` and `<cloudtrail_cloudwatch_log_group>` as appropriate.

```bash
aws cloudformation update-stack --template-body file://metric-filters-and-alarms.cfn.yml --stack-name Metric-Filters-And-Alarms --parameters ParameterKey=NotificationEmailAddress,ParameterValue=<email_address_for_notifications> ParameterKey=CloudTrailLogGroup,ParameterValue=<cloudtrail_cloudwatch_log_group>
```

## How to contribute

If you would like to contribute, please open an issue or create a PR with your proposed changes.

## Mentions

This architecture is based on guidelines defined in Section 4 (Monitoring) of CIS Amazon Web Services Foundations v1.4.0.
