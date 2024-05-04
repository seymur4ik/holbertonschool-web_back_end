#!/usr/bin/env python3
"""
Model that defines a type-annotated function element_length
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of integers representing the lengths of the strings in lst.
    """
    return [len(i) for i in lst]
