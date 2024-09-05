#!/usr/bin/python3
"""An algorithm that determines who is the winner of a game."""


def is_prime(n):
    """A function that checks if a number is a prime number.
        args(int): it takes an integer.
        return: (bool) it returns True if the number is prime else false.
    """
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 0:
        return False
    max_factor = round(n ** 0.5) + 1
    for factor in range(5, max_factor, 6):
        if n % factor == 0:
            return False
        if n % (factor + 2) == 0:
            return False
    return True


def eliminate(prime_number, list_of_numbers):
    """A function that removes a number and its multiples from a list."""
    list_of_numbers.remove(prime_number)
    for number in list_of_numbers:
        if number % prime_number == 0:
            list_of_numbers.remove(number)


def isWinner(x, nums):
    """A function that determines the winner of a game."""
    turn = 0
    Ben_wins = 0
    Maria_wins = 0
    prime_found = None
    for round in range(0, x):
        numbers = [x for x in range(1, nums[round] + 1)]
        for number in numbers:
            prime_found = is_prime(number)
            if prime_found is True:
                eliminate(number, numbers)
                if turn == 0:
                    turn = 1
                if turn == 1:
                    turn = 0
            else:
                if turn == 0:
                    Ben_wins += 1
                if turn == 1:
                    Maria_wins += 1
        if prime_found is False:
            if turn == 0:
                Maria_wins += 1
                turn += 1
            else:
                Ben_wins += 1
                turn = turn - 1
    if Ben_wins > Maria_wins:
        return 'Ben'
    elif Maria_wins > Ben_wins:
        return 'Maria'
    return None
