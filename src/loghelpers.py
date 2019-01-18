"""Collection of functions to deal with CloudWatch logs."""
import base64
import gzip
import json
import config

ID = 'id'
TIMESTAMP = 'timestamp'
MESSAGE = 'message'


def extract_log_events(event):
    """Decode and decompress log data."""
    log_data = event['awslogs']['data']
    compressed_data = base64.b64decode(log_data)
    decompressed_data = gzip.decompress(compressed_data)
    json_data = json.loads(decompressed_data)
    log_events = json_data['logEvents']
    return log_events


def condense_log_events(log_events):
    """Condense log events into single strings."""
    condensed_events = []
    for event in log_events:
        if config.MESSAGE_ONLY == 'False':
            condensed_events.append(json.dumps(event))
        else:
            condensed_events.append(event.get(MESSAGE))
    return condensed_events
