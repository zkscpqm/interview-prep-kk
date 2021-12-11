"""
Task specification:

Given a list L containing n integers {l(1), l(2).... l(n)}, return a list R containing all positive integers in L
if the corresponding negative also exists in L. A single negative number allows all positive counterparts to be added.

Constraints:
    For each l in L: -10 <= l <= 10; l ∈ ℤ
    Maximum complexity allowed is O(2n)

Example:

>>> L = [1, 2, -3, -4, 4, 3, 3, 2, 1]
>>> R = [4, 3, 3]

"""

from typing import List, Set


def find_pos_neg_couples(inp: List[int]) -> List[int]:
    ret: List[int] = []
    negs: Set = set()
    for i in inp:
        if i<0:
            negs.add(i)

    for i in inp:
        if i*-1 in negs:
            ret.append(i)

    return ret
