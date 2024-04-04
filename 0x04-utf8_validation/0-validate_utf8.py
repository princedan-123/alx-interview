#!/usr/bin/python3
"""A Python script checks if a dataset represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
        A function that validates a byte of data, checking if it is
        a valid utf-8 encoding.
        args:data(list) a list of integers.
        return: True or False
    """
    validate = None
    for byte in data:
        if isinstance(byte, int):
            if byte >= 0 and byte <= 127:
                validate = True
            else:
                validate = False
                break
    return validate
