#!/usr/bin/python3
'''
Minimum Operations' main module
'''


def is_prime(n):
    '''
    description: check if a number is prime
    Args:
        n(int): number to check
    Return: boolean
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def prime_factors_of_number(n):
    '''
    Descriprion: check for prime factors of a number
    Args: (n) the number
    Return: list of primes factors of number
    '''

    factors = []

    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)

    return factors


def minOperations(n):
    '''
    description: A function to determine the minimum number of operations
        to fullfil the total count (value of n)
        of character 'H' through copy and paste
    Args:
        n (int): number of 'H' character
    Return: an integer
    '''
    if n <= 1:
        return 0

    factors = prime_factors_of_number(n)
    highest_factor = factors[len(factors) - 1]

    # the lenght will intially be at the same level with the operations
    # Note that the value is the highest factor.
    # for operations it would some to that value since it would involve
    # first copy and consiquent pasting of only one H value
    length = highest_factor
    operations = highest_factor

    if length != n:
        # time for paste operation
        while length <= n:
            operations += 1
            length += highest_factor

    return operations
