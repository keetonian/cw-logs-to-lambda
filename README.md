# cw-logs-to-lambda

This serverless app publishes AWS CloudWatch logs to another Lambda function based on a subscription filter. It does this by extracting the information from a CloudWatch log event and sending a JSON array of strings with information from the logs.

## App Architecture

![App Architecture](https://github.com/keetonian/cw-logs-to-lambda/raw/master/images/cw-logs-to-lambda.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository]() and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

### Destination Function Name
Pass in a function name either as a reference parameter from another stack or resource or by supplying a name.

### Log Group Name
You can find the name of the log group by navigating to CloudWatch logs on the AWS console. You can also pass it in as a parameter from another stack or another resource (e.g. default lambda log group names are `/aws/lambda/{lambda-function-name}`).

### Filter Pattern
CloudWatch logs allow you to filter logs based on a pattern. For more information, see the [AWS Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

## App Parameters

1. `DestinationFunctionName` (required) - Name of the function to which this application will send log messages
1. `LogGroupName` (required) - Log group to listen to (has to be in same account and region)
1. `FilterPattern` (optional) - Pattern for filtering log events. Default: ERROR
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `LogsToLambdaName` - Lambda function name.
1. `LogsToLambdaArn` - Lambda function ARN.

## License Summary

This code is made available under the MIT license. See the LICENSE file.