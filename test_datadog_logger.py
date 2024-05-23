import pytest
from datadog_logger import DatadogLogger
from datadog import api

@pytest.fixture
def datadog_logger(mocker):
    mocker.patch('datadog.initialize')
    return DatadogLogger(api_key='dummy_api_key', app_key='dummy_app_key')

def test_info_logging(mocker, datadog_logger):
    mock_create_event = mocker.patch.object(api.Event, 'create')
    datadog_logger.info('This is an info message')
    mock_create_event.assert_called_once_with(title="Data Pipeline Log", text='This is an info message', alert_type="info")

def test_error_logging(mocker, datadog_logger):
    mock_create_event = mocker.patch.object(api.Event, 'create')
    datadog_logger.error('This is an error message')
    mock_create_event.assert_called_once_with(title="Data Pipeline Log", text='This is an error message', alert_type="error")

def test_warning_logging(mocker, datadog_logger):
    mock_create_event = mocker.patch.object(api.Event, 'create')
    datadog_logger.warning('This is a warning message')
    mock_create_event.assert_called_once_with(title="Data Pipeline Log", text='This is a warning message', alert_type="warning")

def test_debug_logging(mocker, datadog_logger):
    mock_create_event = mocker.patch.object(api.Event, 'create')
    datadog_logger.debug('This is a debug message')
    mock_create_event.assert_called_once_with(title="Data Pipeline Log", text='This is a debug message', alert_type="debug")
