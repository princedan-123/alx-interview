#!/usr/bin/python3
"""A python script that parses log files"""
import re
import signal
import sys

file_size = []
status_code = []
line_number = 1


def signal_handler(status_code, file_size, print_result):
    """
        A function that is executed when SIGINT is encountered.
        Args: signal(int) signal number.
              frame(Callable) instance of call stack.
              status_code(List) list of status_code
              file_size(List) list of file sizes.
              print_result(Callable) called to print the final result.
        Result: None.
    """
    def handler(signal, frame):
        """A closure function."""
        print_result(count_occurrence, print_status_code, status_code, total_size)
    return handler


def count_occurrence(status_code=None):
    """
    A function that counts the number of status_code in a list
    Args: status_code(list) contains the status code to be counted
    Return: A dictionary of status code and its occurrence is returned
    """
    counted = {}
    check = set()
    if status_code is not None:
        status_code.sort()
        for code in status_code:
            occurrence = status_code.count(code)
            if code not in check:
                counted[code] = occurrence
                check.add(code)
    else:
        return None
    return counted


def print_status_code(status_code=None):
    """
        A function that prints status code
        Args: status_code(dictionary) contains status code and its occurrences
        Return: None
    """
    if status_code is not None:
        for key, value, in status_code.items():
            print(f'{key}: {value}')


def print_result(count_occurrence, print_status_code, status_code, file_size):
    """
        A function that prints the final result.
        Args: count_occurrence(Callable) counts the occurrences of status code.
              print_status_code(Callable) print status code.
              status_code(List) contains the status code.
        Return: None
    """
    counted_code = count_occurrence(status_code)
    if counted_code is None or len(status_code) == 0:
        return None
    print(f'File size: {file_size}')
    print_status_code(counted_code)


signal.signal(signal.SIGINT, signal_handler(status_code, file_size, print_result))

pattern = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d*\] \"GET /projects/260 HTTP/1\.1\" \d{3} \d+"
for line in sys.stdin:
    line = line.strip()
    pattern_match = re.fullmatch(pattern, line)
    if pattern_match is not None:
        print('matched')
        text = pattern_match.group()
        text_list = text.split(' ')
        file_size.append(int(text_list[-1]))
        status_code.append(int(text_list[-2]))
        if line_number == 10:
            total_size = sum(file_size)
            print_result(count_occurrence, print_status_code, status_code, total_size)
            line_number -= 10
    line_number += 1
