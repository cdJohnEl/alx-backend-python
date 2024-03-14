#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
"""


import typing

def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats"""
    return float(sum(mxd_list))
