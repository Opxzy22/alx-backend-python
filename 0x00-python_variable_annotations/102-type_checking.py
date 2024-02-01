#!/usr/bin/env python3
"""
    Defines the zoom_array function
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        zoon_array: returns a list generated from a tuple.

        Args:
            lst (Tuple): a tuple of any datatype
            factor (int, optional): Defaults to 2.

        Returns:
            List: returns a list
    """
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)