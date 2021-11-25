"""
Task specification:

Given a positive integer 'x', return a set 'S' = {0, 1, 2.... x} containing all integers where:
 - 0 <= s <= x
 - All 0-bits in 'x' are also 0 in 's'

Maximum complexity allowed is O(n)

Extra info:
 - x ∈ { 0, 1, 2..., 2**16 } ∈ ℕ

Tip:
    In Python, you can define integers by their binary representations by prefixing with 0x
    The following two ways to define 10 are identical:
        >>> x = 10
        >>> y = 0x1010

Example:
    Note how 10(0x1010) has zeros in the 'one' and 'four' bits and ones in the 'eight' and 'two' bit
    positions. All results therefore also have zeros in 'one' and 'four' bits and all other bits are
    irrelevant.

>>> x = 10  # In Binary: 1010
>>> S = {0x0000, 0x1000, 0x0010, 0x1010}

Hints:
    - Do you have to think about the bit which stores the negative sign?
    - Converting an int 'x' to its binary representation is done like: bin(x)

"""
from typing import Set


def bit_masks(inp: int) -> Set[int]:
    return_value: Set[int] = set()

    return return_value
