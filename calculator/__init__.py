"""
Calculator package initialization.
Exports main calculator functions and operations.
"""

from calculator.basic_operations import (
    calculate_sum,
    calculate_product,
    print_sum_and_product,
    sum_and_product
)

__all__ = [
    'calculate_sum',
    'calculate_product',
    'print_sum_and_product',
    'sum_and_product'
]