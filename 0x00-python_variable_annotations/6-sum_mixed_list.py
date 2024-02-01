#!/usr/bin/env python3
"""sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that takes a list of int and floats
        returns their sum as a float
    """
    return sum(mxd_lst)
