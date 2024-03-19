#!/usr/bin/python3
"""A program that determines the minimum number of operations."""
from typing import List


def is_prime(n: int):
    """
    A function that creates a list of prime numbers within the range
    of n.
    Args: n (int).
    Return: a list of prime numbers within the range of n begining from 2.
    """
    prime = []
    inclusive = n + 1
    if n == 2:
        prime.append(2)
        return prime
    for number in range(2, inclusive):
        if number == 2 or number == 3 or number == 5 or number == 7:
            prime.append(number)
        elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            prime.append(number)
    return prime


def minOperations(n: int) -> int:
    """
    A function that uses prime factorization to determine the minimum 
    number of operation that can be performed when writing n number of H into a
    code editor.
    Arg: n (int) number of H to be written
    Return: returns an integer that represents the minimum number of operation
    """
    if not isinstance(n, int):
        return 0
    elif n < 2:
        return 0
    elif n == 2:
        return n
    dividend = n
    divisible = None
    track = 0
    prime_numbers = is_prime(dividend)
    for number in prime_numbers:
        if dividend % number == 0:
            divisible = True
            while divisible:
                quotient =  dividend / number
                track += number
                if quotient == 0:
                    return track
                elif quotient % number == 0:
                    divisible = True
                    dividend = quotient
                else:
                    divisible = False
                    dividend = quotient
    return track
