"""
Basic mathematical operations module.
Provides functions to calculate and print sum and product of two numbers.
"""


def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Returns:
        float or int: Sum of the two numbers
    
    Raises:
        ValueError: If either argument cannot be converted to a number
    """
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 + n2
        
        # Return as int if the result is a whole number
        if result.is_integer():
            return int(result)
        return result
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")


def calculate_product(num1, num2):
    """
    Calculate the product of two numbers.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Returns:
        float or int: Product of the two numbers
    
    Raises:
        ValueError: If either argument cannot be converted to a number
    """
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 * n2
        
        # Return as int if the result is a whole number
        if result.is_integer():
            return int(result)
        return result
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")


def print_sum_and_product(num1, num2):
    """
    Calculate and print both the sum and product of two numbers.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Raises:
        ValueError: If either argument cannot be converted to a number
    """
    try:
        # Calculate sum and product
        sum_result = calculate_sum(num1, num2)
        product_result = calculate_product(num1, num2)
        
        # Convert inputs to appropriate type for display
        n1 = float(num1)
        n2 = float(num2)
        
        if n1.is_integer():
            n1 = int(n1)
        if n2.is_integer():
            n2 = int(n2)
        
        # Print results
        print(f"Numbers: {n1} and {n2}")
        print(f"Sum: {n1} + {n2} = {sum_result}")
        print(f"Product: {n1} × {n2} = {product_result}")
        
    except ValueError as e:
        print(f"Error: {e}")
        raise


def sum_and_product(num1, num2):
    """
    Calculate and return both the sum and product of two numbers.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Returns:
        dict: Dictionary containing sum and product results
    
    Raises:
        ValueError: If either argument cannot be converted to a number
    """
    sum_result = calculate_sum(num1, num2)
    product_result = calculate_product(num1, num2)
    
    return {
        'sum': sum_result,
        'product': product_result,
        'num1': num1,
        'num2': num2
    }