#!/usr/bin/env python3
"""
    Defines the make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        make_multiplier: return a function that multipliers the arg by itself.

    Args:
        multiplier (float): float argument

    Returns:
        Callable[[float], float]: a function that returns a float of the
        argument.
    """
    def multi(x: float) -> float:
        """
            wrapper: this is a function wrapper that returns the
            sqaured value of it parameter

        Args:
            x (float): float argument

        Returns:
            float: returns squared arg
        """
        return multiplier * x

    return multi