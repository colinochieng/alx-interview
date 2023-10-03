#!/usr/bin/python3
"""
Module for implementing lockboxes function
Module challenge: You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and each box may
    contain keys to the other boxes.
"""
from typing import List, Set


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    description: checks if all boxes in the array are
        likely to be opened.
        A key with the same number as a box opens that box
        A key is a value inside each of the box. It can only be obtained after
        opening a box. The first box boxes[0] is unlocked

    Args:
        boxes(list[list]):  is a list of lists
    assumption:
        all keys will be positive integers
        There can be keys that do not have boxes
    Return: True if all boxes can be opened, else return False
    """
    if len(boxes) == 0 or len(boxes) == 1:
        return True

    # use sets to avoid duplicacy in keys if found
    # + in multiple boxes
    availedKeys: Set = set(boxes[0])
    trackAvailedKeys: Set = set()
    stillLockedBoxes: Set = set()
    openedBoxes: Set = {0}

    if len(boxes) == 2:
        if 1 in availedKeys:
            return True

    for idx in range(1, len(boxes)):
        if idx in availedKeys:
            availedKeys.update(set(boxes[idx]))
        else:
            stillLockedBoxes.add(idx)

    if len(stillLockedBoxes) > 0:
        availedKeys = availedKeys - openedBoxes
        trackAvailedKeys = set(availedKeys)

        keyFound = True
        while keyFound and len(stillLockedBoxes) > 0 and len(availedKeys) > 0:
            len_opened_boxes = len(openedBoxes)
            for key in availedKeys:
                if key in stillLockedBoxes:
                    openedBoxes.add(key)
                    stillLockedBoxes.remove(key)
                    trackAvailedKeys.update(set(boxes[key]))

            # differentiate forms to reduce iterations
            availedKeys = trackAvailedKeys - openedBoxes

            if len(openedBoxes) == len_opened_boxes:
                keyFound = False

        if len(stillLockedBoxes) > 0:
            return False

    return True
