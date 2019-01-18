"""Functions to help with integrating with other lambdas."""
import config
import boto3
import lambdalogging
import json

LOG = lambdalogging.getLogger(__name__)


def send_message_array(messages):
    """Send messages to another lambda function."""
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=config.LAMBDA_NAME,
        InvocationType='Event',
        Payload=json.dumps(messages)
    )
    LOG.info("Function response: %s", response)
