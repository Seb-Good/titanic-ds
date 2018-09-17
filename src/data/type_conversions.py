"""
type_conversions.py
-------------------
This module provides a functions for converting data types.
By: Sebastian D. Goodfellow, Ph.D., 2018
"""

# Compatibility imports
from __future__ import absolute_import, division, print_function

# 3rd party imports
import numpy as np


def sex_type_conversion(sex):
    """Male=0 and Female=1"""
    if sex == 'male':
        return 0
    elif sex == 'female':
        return 1
    else:
        return np.nan


def embarked_type_conversion(embarked):
    """S=0, C=1, and Q=2"""
    if embarked == 'S':
        return 0
    elif embarked == 'C':
        return 1
    elif embarked == 'Q':
        return 2
    else:
        return np.nan
