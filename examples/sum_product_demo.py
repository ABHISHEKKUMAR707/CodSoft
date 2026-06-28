#!/usr/bin/env python3
"""
Sum and Product Demonstration Script

This script demonstrates the usage of sum and product calculation functions
from the calculator.basic_operations module.
"""

import sys
import os

# Add parent directory to path to import calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.basic_operations import (
    calculate_sum,
    calculate_product,
    print_sum_and_product,
    sum_and_product
)


def main():
    """
    Main function to demonstrate sum and product calculations.
    """
    print("=" * 60)
    print("Sum and Product Calculator - Demonstration")
    print("=" * 60)
    print()
    
    # Example 1: Using print_sum_and_product function
    print("Example 1: Calculate sum and product of 10 and 5")
    print("-" * 60)
    print_sum_and_product(10, 5)
    print()
    
    # Example 2: Using print_sum_and_product with different numbers
    print("Example 2: Calculate sum and product of 7.5 and 3.2")
    print("-" * 60)
    print_sum_and_product(7.5, 3.2)
    print()
    
    # Example 3: Using individual functions
    print("Example 3: Using individual functions for 15 and 4")
    print("-" * 60)
    num1, num2 = 15, 4
    sum_result = calculate_sum(num1, num2)
    product_result = calculate_product(num1, num2)
    print(f"Numbers: {num1} and {num2}")
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")
    print()
    
    # Example 4: Using sum_and_product function (returns dict)
    print("Example 4: Using sum_and_product function for 12 and 8")
    print("-" * 60)
    results = sum_and_product(12, 8)
    print(f"Numbers: {results['num1']} and {results['num2']}")
    print(f"Sum: {results['sum']}")
    print(f"Product: {results['product']}")
    print()
    
    # Example 5: Negative numbers
    print("Example 5: Calculate sum and product of -6 and 9")
    print("-" * 60)
    print_sum_and_product(-6, 9)
    print()
    
    # Example 6: Zero
    print("Example 6: Calculate sum and product of 20 and 0")
    print("-" * 60)
    print_sum_and_product(20, 0)
    print()
    
    # Example 7: Error handling
    print("Example 7: Error handling with invalid input")
    print("-" * 60)
    try:
        print_sum_and_product("abc", 5)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print()
    
    # Interactive mode
    print("=" * 60)
    print("Interactive Mode")
    print("=" * 60)
    print()
    
    try:
        user_num1 = input("Enter first number (or press Enter to skip): ").strip()
        if user_num1:
            user_num2 = input("Enter second number: ").strip()
            print()
            print("Results:")
            print("-" * 60)
            print_sum_and_product(user_num1, user_num2)
            print()
    except ValueError as e:
        print(f"Error: {e}")
        print()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        print()
    
    print("=" * 60)
    print("Demonstration Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()