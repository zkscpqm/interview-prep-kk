"""
Task specification:

Given a list of websites/endpoints/links and a domain, return True or False for whether they're valid corporate links.

What is a valid corporate link:
    - Can either have no protocol OR http:// OR https://
    - Is in the address space of the given domain (eg: '*.store.com') where * means anything
        - Aka this is also valid: api.store.com/
        - This too: admin.store.com/
        - This too: https://many.paths.back.store.com/
        - This is not: store.com.other/
        - This is also not: my.store.net/

Example:

>>> domain = '*.store.com'
>>> endpoints = ['store.com/new-items', 'https://api.store.com/items/1', 'api.store/items/1']
>>> ret = [True, True, False]

"""

from typing import List


def validate_endpoints(domain: str, endpoints: List[str]) -> List[bool]:
    rv = []

    return rv
