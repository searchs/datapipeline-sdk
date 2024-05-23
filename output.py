import json

class DataOutput:
    @staticmethod
    def to_file(data, filename):
        with open(filename, 'w') as f:
            if isinstance(data, dict):
                json.dump(data, f, indent=2)
            elif isinstance(data, str):
                f.write(data)
            else:
                raise ValueError("Unsupported data type for output.")

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as f:
            if filename.endswith('.json'):
                return json.load(f)
            else:
                return f.read()

# Example Usage
# data = {"key": "value"}
# DataOutput.to_file(data, 'output.json')
# print(DataOutput.from_file('output.json'))
