from datetime import datetime
from .operations import log_operation

class Calculator:
    """A complete calculator class with detailed operation logging"""
    
    def __init__(self):
        self.history = []
    
    def add(self, num1, num2):
        """
        Add two numbers together with detailed logging.
        
        Args:
            num1 (float or int): First number
            num2 (float or int): Second number
        
        Returns:
            dict: Result with operation details
        
        Raises:
            ValueError: If either argument cannot be converted to a number
        """
        try:
            n1 = float(num1)
            n2 = float(num2)
            result = n1 + n2
            
            # Convert to int if whole number
            if result.is_integer():
                result = int(result)
                n1 = int(n1) if n1.is_integer() else n1
                n2 = int(n2) if n2.is_integer() else n2
            
            operation_detail = log_operation('addition', n1, n2, result)
            self.history.append(operation_detail)
            
            return operation_detail
            
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")
    
    def subtract(self, num1, num2):
        """
        Subtract two numbers with detailed logging.
        
        Args:
            num1 (float or int): First number
            num2 (float or int): Second number
        
        Returns:
            dict: Result with operation details
        
        Raises:
            ValueError: If either argument cannot be converted to a number
        """
        try:
            n1 = float(num1)
            n2 = float(num2)
            result = n1 - n2
            
            # Convert to int if whole number
            if result.is_integer():
                result = int(result)
                n1 = int(n1) if n1.is_integer() else n1
                n2 = int(n2) if n2.is_integer() else n2
            
            operation_detail = log_operation('subtraction', n1, n2, result)
            self.history.append(operation_detail)
            
            return operation_detail
            
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")
    
    def multiply(self, num1, num2):
        """
        Multiply two numbers with detailed logging.
        
        Args:
            num1 (float or int): First number
            num2 (float or int): Second number
        
        Returns:
            dict: Result with operation details
        
        Raises:
            ValueError: If either argument cannot be converted to a number
        """
        try:
            n1 = float(num1)
            n2 = float(num2)
            result = n1 * n2
            
            # Convert to int if whole number
            if result.is_integer():
                result = int(result)
                n1 = int(n1) if n1.is_integer() else n1
                n2 = int(n2) if n2.is_integer() else n2
            
            operation_detail = log_operation('multiplication', n1, n2, result)
            self.history.append(operation_detail)
            
            return operation_detail
            
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")
    
    def divide(self, num1, num2):
        """
        Divide two numbers with detailed logging.
        
        Args:
            num1 (float or int): First number
            num2 (float or int): Second number
        
        Returns:
            dict: Result with operation details
        
        Raises:
            ValueError: If either argument cannot be converted to a number
            ZeroDivisionError: If attempting to divide by zero
        """
        try:
            n1 = float(num1)
            n2 = float(num2)
            
            if n2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            
            result = n1 / n2
            
            # Convert to int if whole number
            if result.is_integer():
                result = int(result)
                n1 = int(n1) if n1.is_integer() else n1
                n2 = int(n2) if n2.is_integer() else n2
            
            operation_detail = log_operation('division', n1, n2, result)
            self.history.append(operation_detail)
            
            return operation_detail
            
        except ZeroDivisionError:
            raise
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid input: both arguments must be numbers. Got {type(num1)} and {type(num2)}")
    
    def get_history(self):
        """Get the calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear the calculation history"""
        self.history = []