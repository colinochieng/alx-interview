#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__("0-making_change").makeChange

print(makeChange([1, 2, 25], 37))  # 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # -1
print(makeChange([1, 5, 10, 25], 63))  # Output: 6 (since 63 = 25 + 25 + 10 + 1 + 1 + 1)
print(makeChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
print(makeChange([10, 20, 50], 70))  #  Output: 2 (70 = 50 + 20)
print(makeChange([3, 7, 9], 13))  # Output: -1 (No combination of coins can make 13)
print(makeChange([1, 2, 2, 5], 7))  # Output: 2 (7 = 5 + 2)
print(makeChange([1, 2, 5], 0))  # Output: 0 (No coins needed for total 0)
print(makeChange([1, 2, 5], -5))  # Output: 0 (No coins needed for negative total)
print(makeChange([10], 30))  # Output: 3 (30 = 10 + 10 + 10)
print(makeChange([], 8))  # Output: -1 (No coins available)
print(makeChange([1, 2, 5], 100))  # Output: 20 (100 = 5 * 20)
print(makeChange([2, 7, 12, 18, 22], 42))  # Output: 3 (42 = 22 + 18 + 2)
