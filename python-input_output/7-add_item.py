#!/usr/bin/python3
"""Module script that adds all arguments to a Python list,
and then save them to a file"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    if os.path.exists(filename):
        data = load_from_json_file(filename)
    else:
        data = []
    if len(sys.argv) > 1:
        for item in range(1, len(sys.argv)):
            data.append(sys.argv[item])
    save_to_json_file(data, filename)
