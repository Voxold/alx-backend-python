#!/usr/bin/env python3
"""Module de task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """creates a multiplier function"""
    return lambda x: x * multiplier
