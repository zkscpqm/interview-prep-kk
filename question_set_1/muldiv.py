"""
Task specification:

Given a list 'a' containing N integers { a(0)... a(n) }, return a list 'b' of size N where
each element is the product of all elements from the initial list except a[i]
at each index i.

Maximum complexity allowed is O(2n)

Example:

>>> a = [1, 2, 3, 4]
>>> b = [24, 12, 8, 6]

"""

from typing import List


def mul_div(inp: List[float]) -> List[float]:
    ret: List[float] = []
    total_val: float = 1
    num_zeros: int = 0

    for val in inp:
        if val == 0:
            num_zeros += 1
        else:
            total_val *= val

    if num_zeros > 1:
        return [0 for _ in inp]

    for val in inp:
        if num_zeros != 0:
            if val != 0:
                ret.append(0)
            else:
                ret.append(total_val)
        else:
            ret.append(total_val / val)

    return ret
