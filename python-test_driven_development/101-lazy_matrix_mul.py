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
    try:
        result = np.matmul(m_a, m_b)
    except ValueError as e:
        if "Scalar operands are not allowed" in str(e):
            raise ValueError("Scalar operands are not allowed, use '*' instead")
        else:
            raise
    return result
