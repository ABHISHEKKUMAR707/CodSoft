"""
Simple subtract tool for performing subtraction operations.

This module provides a command-line tool for subtracting two numbers
with proper input validation and error handling.
"""


def subtract(num1, num2):
    """
    Subtract two numbers and return the result.
    
    Args:
        num1 (float or int): First number (minuend)
        num2 (float or int): Second number (subtrahend) to subtract from first
    
    Returns:
        float or int: Difference of the two numbers (num1 - num2)
    
    Raises:
        ValueError: If either argument cannot be converted to a number
    """
    try:
        # Convert to float to handle both int and float inputs
        n1 = float(num1)
        n2 = float(num2)
        
        result = n1 - n2
        
        # Return as int if the result is a whole number
        if result.is_integer():
            return int(result)
        return result
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")


def validate_numeric_input(user_input):
    """
    Validate that user input can be converted to a number.
    
    Args:
        user_input (str): User input string to validate
    
    Returns:
        float: Converted numeric value
    
    Raises:
        ValueError: If input cannot be converted to a number
    """
    try:
        return float(user_input.strip())
    except ValueError:
        raise ValueError(f"'{user_input}' is not a valid number")


def get_number_input(prompt):
    """
    Get a valid numeric input from user with retry mechanism.
    
    Args:
        prompt (str): Prompt message to display to user
    
    Returns:
        float: Valid numeric input from user
    """
    while True:
        try:
            user_input = input(prompt)
            return validate_numeric_input(user_input)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit(0)


def main():
    """
    Main function to run the subtract tool with user interaction.
    
    Prompts user for two numbers and displays the subtraction result.
    Handles all errors gracefully and provides clear feedback.
    """
    print("=" * 50)
    print("         Simple Subtract Tool")
    print("=" * 50)
    print("This tool subtracts the second number from the first number.")
    print("Formula: First Number - Second Number = Result")
    print()
    
    try:
        # Get first number from user
        first_number = get_number_input("Enter the first number (minuend): ")
        
        # Get second number from user
        second_number = get_number_input("Enter the second number (subtrahend): ")
        
        # Perform subtraction
        result = subtract(first_number, second_number)
        
        # Display result with clear formatting
        print()
        print("=" * 30)
        print("CALCULATION RESULT")
        print("=" * 30)
        
        # Format numbers for display (show as int if whole numbers)
        display_first = int(first_number) if first_number.is_integer() else first_number
        display_second = int(second_number) if second_number.is_integer() else second_number
        
        print(f"{display_first} - {display_second} = {result}")
        print("=" * 30)
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure you enter valid numbers.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.")
        exit(1)


if __name__ == "__main__":
    main()