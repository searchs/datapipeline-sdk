from plugin_interface import TransformationPlugin

class SamplePlugin(TransformationPlugin):
    def transform(self, data):
        # Example transformation: adding a new key-value pair
        if isinstance(data, dict):
            data["new_key"] = "new_value"
        return data

# Example Usage
# plugin = SamplePlugin()
# transformed_data = plugin.transform({"key": "value"})
# print(transformed_data)
