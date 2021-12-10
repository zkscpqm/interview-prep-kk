"""
Task specification:

Given a dictionary D with elements of types Dict, List, Int, String and Float and a key value K:

    - Count the number of levels the dictionary has (aka what depth of nested dicts OR lists are there)
    - Count the number of strings
    - Count the number of numeric values (int, float etc)
    - Count how many times the key value appears

Constraints:
    Maximum complexity allowed is O(n)

Note:
    A dictionary without nested containers has 1 level, not 0.
    A list is considered to add depth
    Strings should match regardless of case ('amy' == 'Amy' == 'AMY') This also goes for the key value if it is a string
    If the key value is a string, then any strings containing the key value as a sub string should also be counted
    Eg: Given key_value = 'Acronis' and a string = 'This is acronis', the key value count should add +1

"""
from typing import Any, Dict


def dict_search(inp: Dict, key_value: Any) -> tuple:
    levels = 1
    str_count = 0
    num_count = 0
    key_val_count = 0

    # Your solution here

    return levels, str_count, num_count, key_val_count
