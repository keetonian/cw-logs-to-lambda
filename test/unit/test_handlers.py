import pytest
import handlers
import lambdahelpers
import requests

import test_constants


def test_logs_to_lambda(mocker):
    mocker.patch.object(lambdahelpers, 'send_message_array')
    handlers.logs_to_lambda(test_constants.AWS_LOG_EVENT, None)
    lambdahelpers.send_message_array.assert_called_with(test_constants.EXTRACTED_LOG_EVENTS_JSON)
