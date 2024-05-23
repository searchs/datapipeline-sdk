import pytest
from transformation import Transformer

def test_json_to_dict():
    json_str = '{"key": "value"}'
    result = Transformer.json_to_dict(json_str)
    assert result == {"key": "value"}

def test_dict_to_json():
    data_dict = {"key": "value"}
    result = Transformer.dict_to_json(data_dict)
    expected_result = '{\n  "key": "value"\n}'
    assert result == expected_result

def test_xml_to_dict():
    xml_str = '<root><key>value</key></root>'
    result = Transformer.xml_to_dict(xml_str)
    assert result == {"root": {"key": "value"}}

def test_dict_to_xml():
    data_dict = {"root": {"key": "value"}}
    result = Transformer.dict_to_xml(data_dict)
    expected_result = '<root><key>value</key></root>'
    assert result == expected_result

# Run the tests
# pytest test_transformation.py
