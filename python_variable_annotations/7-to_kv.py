#!/usr/bin/env python3
"""
Module that defines a function that takes a string k and
an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of the float v.
    """
    return (k, v * v)
