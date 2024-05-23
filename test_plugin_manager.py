import pytest
from plugin_manager import PluginManager

def test_plugin_manager():
    plugin_configs = [
        {'module': 'plugins.sample_plugin', 'class': 'SamplePlugin'},
    ]
    plugin_manager = PluginManager(plugin_configs)
    data = {"key": "value"}
    transformed_data = plugin_manager.apply_plugins(data)
    assert transformed_data["new_key"] == "new_value"

# Run the tests
# pytest test_plugin_manager.py
