#!/usr/bin/python3
"""
    Module to find the max integer in a list

    Write a function that multiplies 2 matrices by using
    the module NumPy

    To install it: pip3 install numpy==1.15.0
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix with numpy """
    return np.dot(m_a, m_b)
