#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    previous_element = 0
    number = 0

    for i in reversed(roman_string):
        value = roman[i]
        if value >= previous_element:
            number += value
        else:
            number -= value
        previous_element = value
    return number
