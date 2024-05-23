from kafka import KafkaProducer, KafkaConsumer
import json

class KafkaIngestion:
    def __init__(self, brokers, topic):
        self.brokers = brokers
        self.topic = topic

    def produce(self, message):
        producer = KafkaProducer(bootstrap_servers=self.brokers,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send(self.topic, message)
        producer.flush()

    def consume(self):
        consumer = KafkaConsumer(self.topic,
                                 bootstrap_servers=self.brokers,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        for message in consumer:
            yield message.value

# Example Usage
# ingestion = KafkaIngestion(brokers='localhost:9092', topic='test-topic')
# ingestion.produce({"key": "value"})
# for message in ingestion.consume():
#     print(message)
