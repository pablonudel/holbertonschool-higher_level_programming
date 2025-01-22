#!/usr/bin/python3
def text_indentation(text):
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
