#!/usr/bin/python3
"""
module for Prime Game
"""


def isWinner(x, nums) -> None:
    """
    describe: function to compute the winner of prime game
        between Mary and Ben
    Args:
        x (int):  is the number of rounds to play
        nums (list): array of maximum number to use for a play
    return (Literals["Mary" | "Ben"]):
        -> name of the player that won the most rounds
        -> If the winner cannot be determined, return None
    """

    def is_prime(n):
        """
        describe: function to check if a number is prime
        Arg:
            n (int): number to check
        return: (bool) if number is prime True otherwise False
        """
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_generator(num):
        """
        describe: function to generate prime numbers
            upto the given number
        Args:
            num (int): number to factor from
        return (List): list of prime integers
        """
        prime_list = []

        for _ in range(num + 1):
            if is_prime(_):
                prime_list.append(_)

        return prime_list

    # no game played
    if x <= 0:
        return None

    maria = 0
    ben = 0

    for round in range(x):
        prime_list = prime_generator(nums[round])

        num_primes = len(prime_list)

        if num_primes % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
