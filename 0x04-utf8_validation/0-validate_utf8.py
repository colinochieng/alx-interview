#!/usr/bin/python3
'''
Module for testing on UTF-8 validation
'''


def validUTF8(data):
    """
    desc: Check if a list of integers
        represents a valid UTF-8 sequence.
    Args:
        data (list of int): A list of integers
        representing a sequence of bytes.
    Returns:
        bool: True if the sequence is a
            valid UTF-8 sequence, False otherwise.
    """
    result = all(type(value) == int for value in data)
    if not result:
        return False
    bytes_to_expect = 0

    # Iterate through the list of integers
    for byte in data:
        # Ensure only the 8 least
        # significant bits are considered
        byte &= 0xFF

        # If we are not expecting any bytes,
        # this should be the start of a new character
        if bytes_to_expect == 0:
            # Check the most significant bits to
            # determine the number of bytes for the character
            if byte & 0x80 == 0:
                bytes_to_expect = 0
            elif byte & 0xE0 == 0xC0:
                bytes_to_expect = 1
            elif byte & 0xF0 == 0xE0:
                bytes_to_expect = 2
            elif byte & 0xF8 == 0xF0:
                bytes_to_expect = 3
            else:
                # Invalid starting byte
                return False
        else:
            # For bytes that are part of a multi-byte
            # character, they should start with '10'
            if byte & 0xC0 == 0x80:
                bytes_to_expect -= 1
            else:
                # Invalid continuation byte
                return False

    # After processing all bytes, if bytes_to_expect
    # is still nonzero, it's an incomplete character
    return bytes_to_expect == 0
