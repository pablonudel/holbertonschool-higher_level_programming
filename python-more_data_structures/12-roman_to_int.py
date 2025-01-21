#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if roman_string and isinstance(roman_string, str):
        rti = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
               'X': 10, 'V': 5, 'I': 1}
        for i in range(len(roman_string)):
            if i > 0 and rti[roman_string[i]] > rti[roman_string[i - 1]]:
                res += rti[roman_string[i]] - (rti[roman_string[i - 1]] * 2)
            else:
                res += rti[roman_string[i]]
    return res
