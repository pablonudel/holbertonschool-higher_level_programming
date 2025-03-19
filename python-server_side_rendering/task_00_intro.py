import os
"""Module for generate_invitations method"""

def generate_invitations(template, attendees):
    """generates personalized invitation files from a template 
    with placeholders and a list of objects."""
    if not isinstance(template, str):
        print("Template is not a string")
        return False
    if not isinstance(attendees, list) or not all(isinstance(item, dict) 
                                                  for item in attendees):
        print("Attendees is not a list of dicts")
        return False
    if template == "":
        print("Template is empty, no output files generated.")
        return False
    if attendees == []:
        print("No data provided, no output files generated.")
        return False
        
    x = 1
    for item in attendees:
        new_template = template
        for key, value in item.items():
            if not value:
                new_template = new_template.replace('{' + key + '}', 
                                                    '{}: N/A'.format(key))
            new_template = new_template.replace('{' + key + '}', str(value))
        filename = 'output_{}.txt'.format(x)
        try:
            if os.path.exists(filename):
                print("file '{}' already exists".format(filename))
            else:
                with open('output_{}.txt'.format(x), 'w') as file:
                    file.write(new_template)
        except IOError as e:
            print("Error writing to file '{}': {}".format(filename, e))
        x = x + 1
    return True