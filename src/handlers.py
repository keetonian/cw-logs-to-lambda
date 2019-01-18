"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import lambdalogging
import lambdahelpers
import loghelpers

LOG = lambdalogging.getLogger(__name__)


def logs_to_lambda(event, context):
    """Lambda function handler."""
    LOG.info('Received event: %s', event)
    log_events = loghelpers.extract_log_events(event)
    messages = loghelpers.condense_log_events(log_events)
    lambdahelpers.send_message_array(messages)
