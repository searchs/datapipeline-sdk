import pytest
from output import DataOutput

def test_to_file():
    data = {"key": "value"}
    DataOutput.to_file(data, 'test_output.json')
    with open('test_output.json', 'r') as f:
        content = f.read()
    expected_content = '{\n  "key": "value"\n}'
    assert content == expected_content

def test_from_file():
    data = {"key": "value"}
    DataOutput.to_file(data, 'test_output.json')
    loaded_data = DataOutput.from_file('test_output.json')
    assert loaded_data == data

# Run the tests
# pytest test_output.py
