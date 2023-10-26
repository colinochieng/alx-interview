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
    # Initialize a variable to keep track
    # of the number of continuation bytes expected.
    continuation_bytes = 0

    # Iterate through the list of integers.
    for integer in data:

        # Check if the integer is within
        # + the valid byte range (0 to 255).
        if not 0 <= integer <= 255:
            return False  # Invalid integer value.

        # If we are not expecting any
        # + continuation bytes, check the leading bits.
        if continuation_bytes == 0:
            if integer < 0x80:  # ASCII character (single-byte).
                continue
            elif integer >= 0xC0 and integer <= 0xFD:
                # The leading bits indicate a multi-byte character.
                # Count the number of leading
                # + '1' bits to determine the number
                # + of bytes in this character.
                mask = 0x80
                while (integer & mask):
                    continuation_bytes += 1
                    mask >>= 1

                # The first byte of a multi-byte character
                # + should have the correct number of leading '1' bits.
                if continuation_bytes < 2 or continuation_bytes > 4:
                    return False
                # Decrement to account for this first byte.
                continuation_bytes -= 1
            else:
                return False  # Invalid leading bits.

        else:
            # Check that the current byte is a continuation byte.
            if integer >= 0x80 and integer <= 0xBF:
                continuation_bytes -= 1
            else:
                return False  # Invalid continuation byte.

    # If there are still
    # continuation bytes expected,
    # the sequence is incomplete. returns false else True
    return continuation_bytes == 0
