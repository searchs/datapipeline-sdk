from kafka_ingestion.py import KafkaIngestion
from transformation.py import Transformer
from output.py import DataOutput
from plugins.sample_plugin import SamplePlugin

class DataPipelineSDK:
    def __init__(self, kafka_brokers, kafka_topic):
        self.ingestion = KafkaIngestion(kafka_brokers, kafka_topic)
        self.plugin = SamplePlugin()

    def process_data(self):
        for message in self.ingestion.consume():
            # Transform data using the plugin
            transformed_data = self.plugin.transform(message)

            # Serialize to JSON
            json_data = Transformer.dict_to_json(transformed_data)

            # Output to file
            DataOutput.to_file(json_data, 'output.json')

# Example Usage
# sdk = DataPipelineSDK(kafka_brokers='localhost:9092', kafka_topic='test-topic')
# sdk.process_data()
