#!/usr/bin/env python3
"""define the to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that takes a string and an int/float, 
    and returns a tuple with the string and the square of the int/float (as a float).
    """
    return k, v ** 2