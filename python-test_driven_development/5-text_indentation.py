#!/usr/bin/python3
"""
This module provides a function that prints a text
with 2 new lines after each of these characters: ., ? and :
<text> must be a string.
There should be no space at the beginning or at the end of each printed line.
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    i = 0
    res = ""

    while i < len(text):
        res += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            res += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(res, end="")
