import pytest
from data_pipeline_sdk import DataPipelineSDK

@pytest.fixture
def sdk():
    return DataPipelineSDK(kafka_brokers='localhost:9092', kafka_topic='test-topic')

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

# Run the tests
# pytest test_data_pipeline_sdk.py
