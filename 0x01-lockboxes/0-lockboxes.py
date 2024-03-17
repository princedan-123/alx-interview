#!/usr/bin/python3
"""Implementing lockboxes algorithm."""
from typing import Set


def check_box(keys: Set[int], box: int) -> bool:
    """A fuction that checks if an individual box can be opened.
        ARGS -> keys (set) keys to that might open a box
            -> box (int)  box to be checked
        RETURN -> (boolean) false is returned if a box cannot be opened
    """
    if box not in keys:
        return False
    return True


def canUnlockAll(boxes):
    """A function that checks if keys in a list can open another list.
        if the member of a list is equal to the index of another list,
        then the list can be opened.
        ARGS: boxes -> A list of lists where each list is a box
        RETURN: BOOLEAN -> it returns True if all boxes can be opened else
            False is returned.
    """
    length = len(boxes)
    box_to_check = list(range(1, length))   # the index of each box
    keys = set()   # created set to avoid duplication of keys
    for box in boxes:
        keys.update(box)    # collating all keys into a set
    for box in box_to_check:
        if not check_box(keys, box):
            return False
    return True
