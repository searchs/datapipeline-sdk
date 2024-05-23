from prometheus_client import Counter, start_http_server

class Metrics:
    def __init__(self):
        self.ingested_messages = Counter('ingested_messages', 'Number of messages ingested')
        self.transformed_messages = Counter('transformed_messages', 'Number of messages transformed')
        self.output_messages = Counter('output_messages', 'Number of messages output')

    def start_server(self, port=8000):
        start_http_server(port)
        print(f"Metrics server started on port {port}")

    def increment_ingested(self):
        self.ingested_messages.inc()

    def increment_transformed(self):
        self.transformed_messages.inc()

    def increment_output(self):
        self.output_messages.inc()

# Example Usage
# metrics = Metrics()
# metrics.start_server()
# metrics.increment_ingested()
