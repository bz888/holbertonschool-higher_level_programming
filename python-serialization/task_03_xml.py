import xml.etree.ElementTree as ET


def _value_to_text(value):
    if value is None:
        return ""

    return str(value)


def _value_to_type(value):
    if value is None:
        return "none"

    return type(value).__name__


def _text_to_value(text, value_type):
    if value_type == "bool":
        return text == "True"
    if value_type == "int":
        return int(text)
    if value_type == "float":
        return float(text)
    if value_type == "none":
        return None

    return text


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = _value_to_text(value)
        child.set("type", _value_to_type(value))

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for child in root:
        value_type = child.get("type", "str")
        dictionary[child.tag] = _text_to_value(child.text, value_type)

    return dictionary
