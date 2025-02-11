#!/usr/bin/python3
"""Module for serialize_to_xml and deserialize_from_xml methods"""
import xml.etree.ElementTree as ET
from xml.dom import minidom


def serialize_to_xml(dictionary, filename):
    """serialize the dictionary into XML and save it to the given filename"""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    xml_str = ET.tostring(root)
    formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")

    with open(filename, 'w+') as f:
        f.write(formatted_xml)


def deserialize_from_xml(filename):
    """read the XML data from that filename,
    and return a deserialized Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}

        return dictionary
    except (FileNotFoundError, ET.ParseError) as e:
        print("Error: {}".format(e))
        return None
