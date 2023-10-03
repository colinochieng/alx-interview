#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[_] for _ in range(1, 10)]
# Expects True, as you can use the key in the first box to unlock the rest.
print(canUnlockAll(boxes))

boxes = [[1, 2], [3], [0, 1, 4], [], [5], [], []]
# Expects False
print(canUnlockAll(boxes))

boxes = [[1], [2], [0, 3], [4], [5]]
# Expects True
print(canUnlockAll(boxes))

boxes = [[1, 2], [3], [0, 1, 4], [], [5]]
# Expects True
print(canUnlockAll(boxes))
