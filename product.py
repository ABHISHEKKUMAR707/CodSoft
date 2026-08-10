from datetime import datetime
from typing import Dict, List, Optional, Union


class Product:
    """A product class representing items in inventory with basic attributes."""
    
    def __init__(self, product_id: str, name: str, price: float, description: str = ""):
        """
        Initialize a new product instance.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Product name
            price (float): Product price
            description (str, optional): Product description. Defaults to "".
        
        Raises:
            ValueError: If any required field is invalid
        """
        self.id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """String representation of the product."""
        return f"Product(id={self.id}, name='{self.name}', price=${self.price:.2f})"
    
    def __repr__(self):
        """Detailed string representation of the product."""
        return (f"Product(id='{self.id}', name='{self.name}', price={self.price}, "
                f"description='{self.description}')")
    
    def to_dict(self):
        """Convert product to dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


# Global product inventory
_product_inventory: Dict[str, Product] = {}


def create_product(product_id: str, name: str, price: Union[float, int], description: str = "") -> Product:
    """
    Create a new product and add it to inventory.
    
    Args:
        product_id (str): Unique identifier for the product
        name (str): Product name
        price (Union[float, int]): Product price
        description (str, optional): Product description. Defaults to "".
    
    Returns:
        Product: The created product instance
    
    Raises:
        ValueError: If product data is invalid or product ID already exists
    """
    # Validate input data
    validation_errors = validate_product_data(product_id, name, price, description)
    if validation_errors:
        raise ValueError(f"Product validation failed: {', '.join(validation_errors)}")
    
    # Check if product ID already exists
    if product_id in _product_inventory:
        raise ValueError(f"Product with ID '{product_id}' already exists")
    
    # Create and store the product
    product = Product(product_id, name, float(price), description)
    _product_inventory[product_id] = product
    
    return product


def validate_product_data(product_id: str, name: str, price: Union[float, int], description: str = "") -> List[str]:
    """
    Validate product data and return list of validation errors.
    
    Args:
        product_id (str): Product ID to validate
        name (str): Product name to validate
        price (Union[float, int]): Product price to validate
        description (str, optional): Product description to validate. Defaults to "".
    
    Returns:
        List[str]: List of validation error messages (empty if valid)
    """
    errors = []
    
    # Validate product ID
    if not product_id or not isinstance(product_id, str):
        errors.append("Product ID must be a non-empty string")
    elif len(product_id.strip()) == 0:
        errors.append("Product ID cannot be empty or whitespace only")
    elif len(product_id) > 50:
        errors.append("Product ID cannot exceed 50 characters")
    
    # Validate name
    if not name or not isinstance(name, str):
        errors.append("Product name must be a non-empty string")
    elif len(name.strip()) == 0:
        errors.append("Product name cannot be empty or whitespace only")
    elif len(name) > 200:
        errors.append("Product name cannot exceed 200 characters")
    
    # Validate price
    if not isinstance(price, (int, float)):
        errors.append("Product price must be a number")
    else:
        try:
            price_float = float(price)
            if price_float < 0:
                errors.append("Product price cannot be negative")
            elif price_float > 999999.99:
                errors.append("Product price cannot exceed $999,999.99")
        except (ValueError, TypeError):
            errors.append("Product price must be a valid number")
    
    # Validate description
    if not isinstance(description, str):
        errors.append("Product description must be a string")
    elif len(description) > 1000:
        errors.append("Product description cannot exceed 1000 characters")
    
    return errors


def search_products(query: str = "", search_by: str = "both") -> List[Product]:
    """
    Search for products by ID, name, or both.
    
    Args:
        query (str, optional): Search query string. Defaults to "" (returns all products).
        search_by (str, optional): Search criteria - "id", "name", or "both". Defaults to "both".
    
    Returns:
        List[Product]: List of matching products
    
    Raises:
        ValueError: If search_by parameter is invalid
    """
    if search_by not in ["id", "name", "both"]:
        raise ValueError("search_by must be 'id', 'name', or 'both'")
    
    if not query:
        return list(_product_inventory.values())
    
    query_lower = query.lower().strip()
    matching_products = []
    
    for product in _product_inventory.values():
        match_found = False
        
        if search_by in ["id", "both"]:
            if query_lower in product.id.lower():
                match_found = True
        
        if search_by in ["name", "both"] and not match_found:
            if query_lower in product.name.lower():
                match_found = True
        
        if match_found:
            matching_products.append(product)
    
    return matching_products


def get_product_by_id(product_id: str) -> Optional[Product]:
    """
    Get a specific product by its ID.
    
    Args:
        product_id (str): The product ID to search for
    
    Returns:
        Optional[Product]: The product if found, None otherwise
    """
    return _product_inventory.get(product_id)


def update_product(product_id: str, **kwargs) -> Product:
    """
    Update an existing product's attributes.
    
    Args:
        product_id (str): ID of the product to update
        **kwargs: Keyword arguments for fields to update (name, price, description)
    
    Returns:
        Product: The updated product
    
    Raises:
        ValueError: If product not found or invalid update data
    """
    if product_id not in _product_inventory:
        raise ValueError(f"Product with ID '{product_id}' not found")
    
    product = _product_inventory[product_id]
    
    # Validate and apply updates
    for field, value in kwargs.items():
        if field == "name":
            if not value or not isinstance(value, str) or len(value.strip()) == 0:
                raise ValueError("Product name must be a non-empty string")
            if len(value) > 200:
                raise ValueError("Product name cannot exceed 200 characters")
            product.name = value
            
        elif field == "price":
            if not isinstance(value, (int, float)):
                raise ValueError("Product price must be a number")
            try:
                price_float = float(value)
                if price_float < 0:
                    raise ValueError("Product price cannot be negative")
                if price_float > 999999.99:
                    raise ValueError("Product price cannot exceed $999,999.99")
                product.price = price_float
            except (ValueError, TypeError):
                raise ValueError("Product price must be a valid number")
                
        elif field == "description":
            if not isinstance(value, str):
                raise ValueError("Product description must be a string")
            if len(value) > 1000:
                raise ValueError("Product description cannot exceed 1000 characters")
            product.description = value
            
        else:
            raise ValueError(f"Invalid field '{field}' for product update")
    
    # Update timestamp
    product.updated_at = datetime.now()
    
    return product


def delete_product(product_id: str) -> bool:
    """
    Remove a product from inventory.
    
    Args:
        product_id (str): ID of the product to delete
    
    Returns:
        bool: True if product was deleted, False if not found
    """
    if product_id in _product_inventory:
        del _product_inventory[product_id]
        return True
    return False


def get_all_products() -> List[Product]:
    """
    Get all products in inventory.
    
    Returns:
        List[Product]: List of all products
    """
    return list(_product_inventory.values())


def get_product_count() -> int:
    """
    Get the total number of products in inventory.
    
    Returns:
        int: Number of products in inventory
    """
    return len(_product_inventory)


def clear_inventory() -> int:
    """
    Remove all products from inventory.
    
    Returns:
        int: Number of products that were removed
    """
    count = len(_product_inventory)
    _product_inventory.clear()
    return count