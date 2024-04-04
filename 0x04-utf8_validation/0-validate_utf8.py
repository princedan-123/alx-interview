#!/usr/bin/python3
"""A Python script checks if a dataset represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
        A function that validates a byte of data, checking if it is
        a valid utf-8 encoding.
        args:data(list) a list of integers.
        return: True or False
    """
    for byte in data:
        validate = False
        if isinstance(byte, int):
            binary_string = bin(byte)
            binary = binary_string[2:]
            if len(binary) == 7:
                validate = True
            if len(binary) > 7:
                first_bit = binary[0]
                second_bit = binary[1]
                if first_bit == '1' and second_bit == '1':
                    validate = True
                else:
                    validate = False 
                    return validate
    return validate
