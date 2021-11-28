"""
Task specification:

Given a non-empty list 'L' containing 'n' elements { l(0), l(1)... l(n) }.
Each element 'x = L[i]' represents a 'wall' as being seen from the side (see diagram below).

Calculate how much rain would be caught in this sequence of walls:
 - Assuming every element

Extra info:
 - n >= 3, n ∈ ℕ
 - For every l in L, l ∈ ℕ


Example:
    Given L = [3, 1, 5, 2, 1, 4, 2], we can visualise as follows:

                    █ = Wall
                    o = Rain
        █
        █ o o █
    █ o █ o o █
    █ o █ █ o █ █
    █ █ █ █ █ █ █
    3 1 5 2 1 4 2

BONUS (required for 100%):

 - Make it so a wall of height 0 is considered a hole and water drains through it.

"""
from typing import List


def rain_catcher(inp: List[int]) -> int:
    res = 0

    return res
