#!/usr/bin/python3
import os
"""Module for generate_invitations method"""


def generate_invitations(template, attendees):
    """generates personalized invitation files from a template
    with placeholders and a list of objects."""

    try:
        if not isinstance(template, str):
            raise TypeError("Template is not a string")
        if not isinstance(attendees, list) or not all(isinstance(item, dict)
                                                      for item in attendees):
            raise TypeError("Attendees is not a list of dictionaries")
    except TypeError as e:
        print("TypeError: {}".format(e))
        return

    try:
        if not template.strip():
            raise ValueError("Template is empty, no output files generated.")
        if not attendees:
            raise ValueError("No data provided, no output files generated.")
    except ValueError as e:
        print("ValueError: {}".format(e))
        return

    for x, item in enumerate(attendees, start=1):
        new_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = item.get(key, "N/A")
            if value is None:
                value = "N/A"
            new_template = new_template.replace('{' + key + '}', value)
        filename = 'output_{}.txt'.format(x)
        if os.path.exists(filename):
            print("file '{}' already exists".format(filename))
            continue

        with open(filename, 'w') as file:
            file.write(new_template)
