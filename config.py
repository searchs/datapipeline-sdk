import json

class Config:
    @staticmethod
    def load_config(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

# Example Usage
# config = Config.load_config('config.json')
