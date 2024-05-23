import logging

class Logger:
    @staticmethod
    def setup_logger(name, log_file, level=logging.INFO):
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

# Example Usage
# logger = Logger.setup_logger('data_pipeline', 'data_pipeline.log')
# logger.info('This is an info message')
