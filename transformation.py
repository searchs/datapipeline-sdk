import json
import xml.etree.ElementTree as ET

class Transformer:
    @staticmethod
    def json_to_dict(json_str):
        return json.loads(json_str)

    @staticmethod
    def dict_to_json(data_dict):
        return json.dumps(data_dict, indent=2)

    @staticmethod
    def xml_to_dict(xml_str):
        root = ET.fromstring(xml_str)
        return Transformer._etree_to_dict(root)

    @staticmethod
    def dict_to_xml(data_dict):
        root = Transformer._dict_to_etree(data_dict)
        return ET.tostring(root, encoding='utf-8').decode('utf-8')

    @staticmethod
    def _etree_to_dict(t):
        return {t.tag: {child.tag: child.text for child in t}}

    @staticmethod
    def _dict_to_etree(d):
        def _to_etree(elem, d):
            for key, val in d.items():
                child = ET.Element(key)
                child.text = str(val)
                elem.append(child)
            return elem

        assert isinstance(d, dict) and len(d) == 1
        tag, body = next(iter(d.items()))
        root = ET.Element(tag)
        return _to_etree(root, body)

# Example Usage
# json_str = '{"key": "value"}'
# xml_str = '<root><key>value</key></root>'
# print(Transformer.json_to_dict(json_str))
# print(Transformer.dict_to_json({"key": "value"}))
# print(Transformer.xml_to_dict(xml_str))
# print(Transformer.dict_to_xml({"root": {"key": "value"}}))


