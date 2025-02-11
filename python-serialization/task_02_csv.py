#!/usr/bin/python
"""Module for convert_csv_to_json method"""
import csv
import json

def convert_csv_to_json(csv_file):
    """takes the CSV filename as its parameter
    and writes the JSON data to data.json"""
    obj = []
    with open(csv_file, newline='') as f:
        if not f:
            raise FileNotFoundError("CSV File not found")
        data = csv.DictReader(f)
        for row in data:
            obj.append(row)
    with open("data.json", 'w+', encoding="utf-8") as f:
        if not f:
            raise FileNotFoundError("JSON File not found")
        f.write(json.dumps(obj))
