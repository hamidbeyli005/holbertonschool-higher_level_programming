#!/usr/bin/python3
"""
Module: 5-text_indentation

Function:
    text_indentation(text)

Description:
    Formats input text by printing two new lines after each '.', '?', or ':'.

Usage Example:
    text_indentation("Lorem ipsum dolor sit amet. Consectetur adipiscing elit.")
"""


def text_indentation(text):
    """
    Args:
        text (str): Input text to be formatted.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    line = ''
    for i in text:
        line += i
        if i == ':' or i == '?' or i == '.':
            print(line.strip())
            """print()"""
            line = ''

    if line:
        print(line.strip())
