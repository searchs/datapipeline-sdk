import pytest
from config import Config

def test_load_config(mocker):
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data='{"key": "value"}'))
    config = Config.load_config('config.json')
    mock_open.assert_called_once_with('config.json', 'r')
    assert config == {"key": "value"}
