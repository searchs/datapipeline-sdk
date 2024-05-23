import logging
from datadog import initialize, api

class DatadogLogger:
    def __init__(self, api_key, app_key, log_level=logging.INFO):
        options = {
            'api_key': api_key,
            'app_key': app_key
        }
        initialize(**options)

        self.logger = logging.getLogger('datadog')
        self.logger.setLevel(log_level)

        # Create a Datadog log handler
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)
        api.Event.create(title="Data Pipeline Log", text=message, alert_type="info")

    def error(self, message):
        self.logger.error(message)
        api.Event.create(title="Data Pipeline Log", text=message, alert_type="error")

    def warning(self, message):
        self.logger.warning(message)
        api.Event.create(title="Data Pipeline Log", text=message, alert_type="warning")

    def debug(self, message):
        self.logger.debug(message)
        api.Event.create(title="Data Pipeline Log", text=message, alert_type="debug")

# Example Usage
# datadog_logger = DatadogLogger(api_key='YOUR_API_KEY', app_key='YOUR_APP_KEY')
# datadog_logger.info('This is an info message')
