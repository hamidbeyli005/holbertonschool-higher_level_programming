#!/usr/bin/python3
"""
This is the module 101-lazy_matrix_mul.
It contains one function: 101-lazy_matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    returns the product of m_a and m_b
    """
    return (np.matmul(m_a, m_b))
