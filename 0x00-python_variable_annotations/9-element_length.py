#!/usr/bin/env python3
"""
    Defines the element_length function
"""
from typing import Iterable, Sequence
from typing import List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        element_length: returns a list of index and item.

    Args:
        lst (Iterable[Squence]): Iterable Sequence

    Returns:
        List[Tuple[Sequence]]: returns a list containing a tuple(iterable)
    """
    return [(i, len(i)) for i in lst]