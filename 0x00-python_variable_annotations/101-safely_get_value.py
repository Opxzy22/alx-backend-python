#!/usr/bin/env python3
"""
    Defines the safely_get_value function
"""
from typing import Mapping, TypeVar, Union, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        safely_get_value: get the key if present or return None.

        Args:
            dct (Mapping[Any, Any]): any datatype as key and value
            key (Any): any datatype
            default (Union[T, None], optional): Defaults to None.

        Returns:
            Union[Any, T]: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default