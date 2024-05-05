#!/usr/bin/python3
"""A program that finds the minimum combination of coins that makes a total"""


def greedy(coins, total):
    """
    A function that finds the biggest number in a list.
    args: coins(list) a list of integers.
          total an integer.
    return: a number that is the bigest  in the list but
            less than or equal to the total. If such number
            does not exist return -1
    """
    for coin in coins:
        if coin == 0:
            continue
        if coin <= total:
            return coin
    return -1


def makeChange(coins, total):
    """
    A function that keeps track of change made and returns the lowest
    possible combination of coins that makes up the total.
    args:   coins(list) a list of integers.
            total(integer)
    return: An integer representing the lowest combination of coins that
            makes up the total.
    """
    if total == 0:
        return 0
    coins.sort(reverse=True)
    counter = 0
    greedy_number = None
    while greedy_number != -1:
        greedy_number = greedy(coins, total)
        print('iteration total:', total)
        print('iteration greedy number:', greedy_number)
        if total == 0:
            return counter
        total = total - greedy_number
        if greedy_number != -1:
            counter += 1
        if total != 0 and greedy_number == -1:
            return -1
