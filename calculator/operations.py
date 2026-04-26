from datetime import datetime

def log_operation(operation, num1, num2, result):
    """
    Log a mathematical operation with complete details.
    
    Args:
        operation (str): The type of operation performed
        num1 (float or int): First operand
        num2 (float or int): Second operand
        result (float or int): Result of the operation
    
    Returns:
        dict: Complete operation details
    """
    operation_symbols = {
        'addition': '+',
        'subtraction': '-',
        'multiplication': '*',
        'division': '/'
    }
    
    operation_detail = {
        'operation': operation,
        'symbol': operation_symbols.get(operation, '?'),
        'operand1': num1,
        'operand2': num2,
        'result': result,
        'expression': f"{num1} {operation_symbols.get(operation, '?')} {num2} = {result}",
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'operation_name': operation.title()
    }
    
    return operation_detail

def get_operation_description(operation_detail):
    """
    Get a human-readable description of an operation.
    
    Args:
        operation_detail (dict): Operation details from log_operation
    
    Returns:
        str: Human-readable description
    """
    op = operation_detail['operation']
    num1 = operation_detail['operand1']
    num2 = operation_detail['operand2']
    result = operation_detail['result']
    
    descriptions = {
        'addition': f"Added {num1} and {num2} to get {result}",
        'subtraction': f"Subtracted {num2} from {num1} to get {result}",
        'multiplication': f"Multiplied {num1} by {num2} to get {result}",
        'division': f"Divided {num1} by {num2} to get {result}"
    }
    
    return descriptions.get(op, f"Performed {op} on {num1} and {num2} to get {result}")

def format_number(num):
    """
    Format a number for display, removing unnecessary decimal places.
    
    Args:
        num (float or int): Number to format
    
    Returns:
        str: Formatted number string
    """
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    elif isinstance(num, float):
        return f"{num:.6f}".rstrip('0').rstrip('.')
    return str(num)

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
            raise ValueError(f"Argument {i+1} must be a valid number, got {type(arg)}")
    
    return numbers