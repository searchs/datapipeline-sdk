from kafka_ingestion import KafkaIngestion
from transformation import Transformer
from output import DataOutput
from config import Config
from logger import Logger
from metrics import Metrics
from plugin_manager import PluginManager
from error_handling import IngestionError, TransformationError, OutputError

class DataPipelineSDK:
    def __init__(self, config_file):
        self.config = Config.load_config(config_file)
        self.ingestion = KafkaIngestion(self.config['kafka_brokers'], self.config['kafka_topic'])
        self.plugin_manager = PluginManager(self.config['plugins'])
        self.logger = Logger.setup_logger('data_pipeline', self.config['log_file'])
        self.metrics = Metrics()
        self.metrics.start_server(self.config.get('metrics_port', 8000))

    def process_data(self):
        try:
            for message in self.ingestion.consume():
                self.metrics.increment_ingested()
                self.logger.info(f"Consumed message: {message}")

                # Transform data using the plugin manager
                try:
                    transformed_data = self.plugin_manager.apply_plugins(message)
                    self.metrics.increment_transformed()
                    self.logger.info(f"Transformed data: {transformed_data}")
                except Exception as e:
                    self.logger.error(f"Transformation error: {e}")
                    raise TransformationError(e)

                # Serialize to JSON
                json_data = Transformer.dict_to_json(transformed_data)

                # Output to file
                try:
                    DataOutput.to_file(json_data, self.config['output_file'])
                    self.metrics.increment_output()
                    self.logger.info(f"Data written to {self.config['output_file']}")
                except Exception as e:
                    self.logger.error(f"Output error: {e}")
                    raise OutputError(e)
        except Exception as e:
            self.logger.error(f"Ingestion error: {e}")
            raise IngestionError(e)

# Example Usage
# sdk = DataPipelineSDK(config_file='config.json')
# sdk.process_data()
