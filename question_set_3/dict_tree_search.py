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
from typing import Any, Dict, List, Union


def dict_search(inp: Union[Dict, List], key_value: Any, current_level: int = 1) -> tuple:
    levels = current_level
    str_count = 0
    num_count = 0
    key_val_count = 0

    if isinstance(key_value, str):
        key_value = key_value.casefold()

    interpreted_inp: List = _check_instances(inp)
    for v in interpreted_inp:
        if isinstance(v, str):
            str_count += 1
            if key_value in v.casefold():
                key_val_count += 1

        elif isinstance(v, (int, float)):
            num_count += 1
            if v == key_value:
                key_val_count += 1

        elif isinstance(v, (list, dict)):
            l, s, n, k = dict_search(v, key_value, current_level + 1)
            if l > levels:
                levels = l
            str_count += s
            num_count += n
            key_val_count += k

    return levels, str_count, num_count, key_val_count


def _check_instances(inp: Any) -> List:
    return inp.values() if isinstance(inp, dict) else inp
