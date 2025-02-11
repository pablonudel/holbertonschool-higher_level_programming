#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    with open(filename, 'w+', encoding="utf-8") as f:
        f.write(json.dumps(data))
    pass

def load_and_deserialize(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)
    pass
