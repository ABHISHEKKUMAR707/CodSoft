"""
Product Calculator Module

This module provides functionality to calculate the product of two numbers
with proper input validation, error handling, and user interaction.
"""

import sys


def validate_numbers(*args):
    """
    Validate that all arguments are valid numbers.
    
    Args:
        *args: Numbers to validate
    
    Returns:
        list: List of converted float numbers
    
    Raises:
        ValueError: If any argument is not a valid number
    """
    numbers = []
    for i, arg in enumerate(args):
        try:
            numbers.append(float(arg))
        except (TypeError, ValueError):
            raise ValueError(f"Argument {i+1} must be a valid number, got {type(arg).__name__}")
    
    return numbers


def multiply_two_numbers(num1, num2):
    """
    Multiply two numbers together and return the result.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Returns:
        float or int: Product of the two numbers
    
    Raises:
        ValueError: If either argument is not a valid number
    """
    try:
        # Validate and convert inputs
        validated_nums = validate_numbers(num1, num2)
        n1, n2 = validated_nums
        
        result = n1 * n2
        
        # Return as int if the result is a whole number
        if result.is_integer():
            return int(result)
        return result
        
    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")


def get_number_input(prompt):
    """
    Get a valid number from user input with error handling.
    
    Args:
        prompt (str): The prompt message to display to the user
    
    Returns:
        float: Valid number entered by user
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Error: Please enter a number.")
                continue
            
            # Validate the input
            validated_nums = validate_numbers(user_input)
            return validated_nums[0]
            
        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(0)
        except EOFError:
            print("\nInput terminated. Exiting.")
            sys.exit(0)


def main():
    """
    Main function to handle user interaction and calculate product of two numbers.
    Includes proper error handling for various edge cases.
    """
    print("Product Calculator")
    print("=" * 18)
    print("This program calculates the product of two numbers.")
    print("Press Ctrl+C to exit at any time.\n")
    
    try:
        # Get first number
        num1 = get_number_input("Enter the first number: ")
        
        # Get second number
        num2 = get_number_input("Enter the second number: ")
        
        # Calculate product
        result = multiply_two_numbers(num1, num2)
        
        # Display result with proper formatting
        print(f"\nResult: {num1} × {num2} = {result}")
        
        # Handle special cases
        if result == 0:
            if num1 == 0 or num2 == 0:
                print("Note: The product is zero because one or both numbers are zero.")
        elif result < 0:
            print("Note: The product is negative because the numbers have opposite signs.")
        elif abs(result) > 1e10:
            print("Note: The result is a very large number.")
        elif 0 < abs(result) < 1e-10:
            print("Note: The result is a very small number.")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)


def run_tests():
    """
    Run test cases to verify the functionality of the product calculator.
    """
    print("Running Product Calculator Tests")
    print("=" * 32)
    
    test_cases = [
        # (num1, num2, expected_result, description)
        (5, 3, 15, "Positive integers"),
        (2.5, 4, 10.0, "Float and integer"),
        (0, 10, 0, "Zero multiplication"),
        (-5, 3, -15, "Negative and positive"),
        (-2, -4, 8, "Two negatives"),
        (0.1, 0.2, 0.02, "Small decimals"),
        (100, 0.01, 1.0, "Large and small"),
        (1, 1, 1, "Identity multiplication"),
        (-1, 5, -5, "Negative one"),
        (1000000, 0.000001, 1.0, "Very large and very small")
    ]
    
    passed = 0
    failed = 0
    
    for num1, num2, expected, description in test_cases:
        try:
            result = multiply_two_numbers(num1, num2)
            if abs(result - expected) < 1e-10:  # Handle floating point precision
                print(f"✓ PASS: {description} - {num1} × {num2} = {result}")
                passed += 1
            else:
                print(f"✗ FAIL: {description} - Expected {expected}, got {result}")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: {description} - {str(e)}")
            failed += 1
    
    # Test error cases
    error_test_cases = [
        ("abc", 5, "Invalid string input"),
        (None, 5, "None input"),
        (5, "", "Empty string input"),
        ([], 5, "List input")
    ]
    
    for num1, num2, description in error_test_cases:
        try:
            multiply_two_numbers(num1, num2)
            print(f"✗ FAIL: {description} - Should have raised an error")
            failed += 1
        except ValueError:
            print(f"✓ PASS: {description} - Correctly raised ValueError")
            passed += 1
        except Exception as e:
            print(f"✗ FAIL: {description} - Unexpected error: {str(e)}")
            failed += 1
    
    print(f"\nTest Summary: {passed} passed, {failed} failed")
    return failed == 0


def show_examples():
    """
    Display example usage of the product calculator.
    """
    print("Product Calculator Examples")
    print("=" * 27)
    
    examples = [
        (5, 3, "Basic multiplication"),
        (2.5, 4, "Decimal multiplication"),
        (0, 100, "Multiplication by zero"),
        (-5, 3, "Negative number multiplication"),
        (-2, -4, "Two negative numbers"),
        (0.1, 0.3, "Small decimal multiplication")
    ]
    
    for num1, num2, description in examples:
        result = multiply_two_numbers(num1, num2)
        print(f"{description}: {num1} × {num2} = {result}")


if __name__ == "__main__":
    import sys
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            success = run_tests()
            sys.exit(0 if success else 1)
        elif sys.argv[1] == "--examples":
            show_examples()
            sys.exit(0)
        elif sys.argv[1] == "--help":
            print("Product Calculator - Calculate the product of two numbers")
            print("\nUsage:")
            print("  python product.py          # Interactive mode")
            print("  python product.py --test   # Run test cases")
            print("  python product.py --examples  # Show examples")
            print("  python product.py --help   # Show this help")
            sys.exit(0)
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use --help for available options.")
            sys.exit(1)
    
    # Run main program in interactive mode
    main()