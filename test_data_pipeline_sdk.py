import pytest
from data_pipeline_sdk import DataPipelineSDK
from output import DataOutput

import pytest
from data_pipeline_sdk import DataPipelineSDK
from error_handling import IngestionError, TransformationError, OutputError

@pytest.fixture
def sdk(mocker):
    mocker.patch('data_pipeline_sdk.Config.load_config', return_value={
        'kafka_brokers': 'localhost:9092',
        'kafka_topic': 'test-topic',
        'log_file': 'data_pipeline.log',
        'output_file': 'output.json',
        'datadog_api_key': 'YOUR_API_KEY',
        'datadog_app_key': 'YOUR_APP_KEY',
        'metrics_port': 8000,
        'plugins': [{'module': 'plugins.sample_plugin', 'class': 'SamplePlugin'}]
    })
    return DataPipelineSDK(config_file='config.json')

# @pytest.fixture
# def sdk():
#     return DataPipelineSDK(kafka_brokers='localhost:9092', kafka_topic='test-topic')

def test_kafka_produce_consume(sdk):
    test_message = {"key": "value"}
    sdk.ingestion.produce(test_message)

    for message in sdk.ingestion.consume():
        assert message == test_message
        break

def test_transformation_plugin():
    plugin = SamplePlugin()
    data = {"key": "value"}
    transformed_data = plugin.transform(data)
    assert transformed_data["new_key"] == "new_value"

def test_data_output():
    data = {"key": "value"}
    DataOutput.to_file(data, 'test_output.json')
    loaded_data = DataOutput.from_file('test_output.json')
    assert loaded_data == data


def test_process_data(mocker, sdk):
    # Mock KafkaIngestion
    mock_consume = mocker.patch.object(sdk.ingestion, 'consume', return_value=[{"key": "value"}])

    # Mock PluginManager
    mock_transform = mocker.patch.object(sdk.plugin_manager, 'apply_plugins', return_value={"key": "value", "new_key": "new_value"})

    # Mock DataOutput
    mock_to_file = mocker.patch.object(sdk.output.DataOutput, 'to_file')

    # Run the process_data method
    sdk.process_data()

    # Verify Kafka consumption
    mock_consume.assert_called_once()

    # Verify transformation
    mock_transform.assert_called_once_with({"key": "value"})

    # Verify data output
    mock_to_file.assert_called_once_with('{\n  "key": "value",\n  "new_key": "new_value"\n}', 'output.json')

def test_transformation_error(mocker, sdk):
    mock_consume = mocker.patch.object(sdk.ingestion, 'consume', return_value=[{"key": "value"}])
    mock_transform = mocker.patch.object(sdk.plugin_manager, 'apply_plugins', side_effect=Exception('Transformation error'))
    mock_to_file = mocker.patch.object(sdk.output.DataOutput, 'to_file')
    mock_log_error = mocker.patch.object(sdk.logger, 'error')

    with pytest.raises(TransformationError):
        sdk.process_data()

    mock_log_error.assert_called_with('Transformation error: Transformation error')

def test_output_error(mocker, sdk):
    mock_consume = mocker.patch.object(sdk.ingestion, 'consume', return_value=[{"key": "value"}])
    mock_transform = mocker.patch.object(sdk.plugin_manager, 'apply_plugins', return_value={"key": "value", "new_key": "new_value"})
    mock_to_file = mocker.patch.object(sdk.output.DataOutput, 'to_file', side_effect=Exception('Output error'))
    mock_log_error = mocker.patch.object(sdk.logger, 'error')

    with pytest.raises(OutputError):
        sdk.process_data()

    mock_log_error.assert_called_with('Output error: Output error')

def test_ingestion_error(mocker, sdk):
    mock_consume = mocker.patch.object(sdk.ingestion, 'consume', side_effect=Exception('Ingestion error'))
    mock_transform = mocker.patch.object(sdk.plugin_manager, 'apply_plugins')
    mock_to_file = mocker.patch.object(sdk.output.DataOutput, 'to_file')
    mock_log_error = mocker.patch.object(sdk.logger, 'error')

    with pytest.raises(IngestionError):
        sdk.process_data()

    mock_log_error.assert_called_with('Ingestion error: Ingestion error')

