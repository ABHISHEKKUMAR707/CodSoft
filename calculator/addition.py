def add_two_numbers(num1, num2):
    """
    Add two numbers together and return the result.
    
    Args:
        num1 (float or int): First number
        num2 (float or int): Second number
    
    Returns:
        float or int: Sum of the two numbers
    
    Raises:
        TypeError: If either argument is not a number
        ValueError: If either argument cannot be converted to a number
    """
    try:
        # Convert to float to handle both int and float inputs
        n1 = float(num1)
        n2 = float(num2)
        
        result = n1 + n2
        
        # Return as int if the result is a whole number
        if result.is_integer():
            return int(result)
        return result
        
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")