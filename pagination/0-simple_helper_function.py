#!/usr/bin/env python3
"""
index_range function module
"""


def index_range(page, page_size):
    """
    Returns a tuple of size two
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    range_tuple = (start_index, end_index)
    return range_tuple
