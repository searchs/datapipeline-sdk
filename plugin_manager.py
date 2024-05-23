import importlib

class PluginManager:
    def __init__(self, plugin_configs):
        self.plugins = []
        self.load_plugins(plugin_configs)

    def load_plugins(self, plugin_configs):
        for plugin_config in plugin_configs:
            module_name, class_name = plugin_config['module'], plugin_config['class']
            module = importlib.import_module(module_name)
            plugin_class = getattr(module, class_name)
            self.plugins.append(plugin_class())

    def apply_plugins(self, data):
        for plugin in self.plugins:
            data = plugin.transform(data)
        return data

# Example Usage
# plugin_configs = [
#     {'module': 'plugins.sample_plugin', 'class': 'SamplePlugin'},
# ]
# plugin_manager = PluginManager(plugin_configs)
# data = {"key": "value"}
# transformed_data = plugin_manager.apply_plugins(data)
# print(transformed_data)
