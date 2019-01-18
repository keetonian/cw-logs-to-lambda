"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LAMBDA_NAME = os.getenv('LAMBDA_NAME')
MESSAGE_ONLY = os.getenv('MESSAGE_ONLY')
