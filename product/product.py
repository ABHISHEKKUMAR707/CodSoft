"""
Product management module with comprehensive product operations.
"""
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Union
import re


class Product:
    """
    Product class to represent a product with all necessary attributes.
    """
    
    def __init__(self, name: str, price: float, description: str = "", category: str = "", stock: int = 0):
        """
        Initialize a Product instance.
        
        Args:
            name (str): Product name
            price (float): Product price
            description (str): Product description
            category (str): Product category
            stock (int): Initial stock quantity
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.stock = stock
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __str__(self):
        """String representation of the product."""
        return f"Product(id={self.id}, name={self.name}, price=${self.price:.2f}, stock={self.stock})"
    
    def __repr__(self):
        """Detailed string representation of the product."""
        return self.__str__()


# Global product storage (in production, this would be a database)
_products: Dict[str, Product] = {}


def validate_product_data(name: str, price: Union[float, int, str], description: str = "", category: str = "") -> Dict:
    """
    Validate product data and return cleaned values.
    
    Args:
        name (str): Product name
        price (Union[float, int, str]): Product price
        description (str): Product description
        category (str): Product category
    
    Returns:
        Dict: Validated product data
    
    Raises:
        ValueError: If validation fails
    """
    # Validate name
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Product name must be a non-empty string")
    
    name = name.strip()
    if len(name) > 200:
        raise ValueError("Product name cannot exceed 200 characters")
    
    # Validate price
    try:
        price = float(price)
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if price > 999999.99:
            raise ValueError("Product price cannot exceed $999,999.99")
    except (TypeError, ValueError) as e:
        if "cannot be negative" in str(e) or "cannot exceed" in str(e):
            raise
        raise ValueError("Product price must be a valid number")
    
    # Validate description
    if not isinstance(description, str):
        description = str(description)
    description = description.strip()
    if len(description) > 1000:
        raise ValueError("Product description cannot exceed 1000 characters")
    
    # Validate category
    if not isinstance(category, str):
        category = str(category)
    category = category.strip()
    if len(category) > 100:
        raise ValueError("Product category cannot exceed 100 characters")
    
    return {
        'name': name,
        'price': price,
        'description': description,
        'category': category
    }


def format_price(price: Union[float, int, str]) -> str:
    """
    Format price as currency string.
    
    Args:
        price (Union[float, int, str]): Price to format
    
    Returns:
        str: Formatted price string
    
    Raises:
        ValueError: If price is invalid
    """
    try:
        price = float(price)
        return f"${price:.2f}"
    except (TypeError, ValueError):
        raise ValueError("Invalid price format")


def create_product(name: str, price: Union[float, int, str], description: str = "", category: str = "", stock: int = 0) -> Product:
    """
    Create a new product with validation.
    
    Args:
        name (str): Product name
        price (Union[float, int, str]): Product price
        description (str): Product description
        category (str): Product category
        stock (int): Initial stock quantity
    
    Returns:
        Product: Created product instance
    
    Raises:
        ValueError: If validation fails
    """
    # Validate basic product data
    validated_data = validate_product_data(name, price, description, category)
    
    # Validate stock
    try:
        stock = int(stock)
        if stock < 0:
            raise ValueError("Stock quantity cannot be negative")
    except (TypeError, ValueError) as e:
        if "cannot be negative" in str(e):
            raise
        raise ValueError("Stock quantity must be a valid integer")
    
    # Create product
    product = Product(
        name=validated_data['name'],
        price=validated_data['price'],
        description=validated_data['description'],
        category=validated_data['category'],
        stock=stock
    )
    
    # Store product
    _products[product.id] = product
    
    return product


def get_product(product_id: str) -> Optional[Product]:
    """
    Get a product by its ID.
    
    Args:
        product_id (str): Product ID
    
    Returns:
        Optional[Product]: Product instance or None if not found
    """
    if not isinstance(product_id, str) or not product_id.strip():
        return None
    
    return _products.get(product_id.strip())


def update_product(product_id: str, name: str = None, price: Union[float, int, str] = None, 
                  description: str = None, category: str = None, stock: int = None) -> Optional[Product]:
    """
    Update an existing product.
    
    Args:
        product_id (str): Product ID
        name (str, optional): New product name
        price (Union[float, int, str], optional): New product price
        description (str, optional): New product description
        category (str, optional): New product category
        stock (int, optional): New stock quantity
    
    Returns:
        Optional[Product]: Updated product instance or None if not found
    
    Raises:
        ValueError: If validation fails
    """
    product = get_product(product_id)
    if not product:
        return None
    
    # Validate and update fields if provided
    if name is not None:
        validated_data = validate_product_data(name, product.price)
        product.name = validated_data['name']
    
    if price is not None:
        validated_data = validate_product_data(product.name, price)
        product.price = validated_data['price']
    
    if description is not None:
        validated_data = validate_product_data(product.name, product.price, description)
        product.description = validated_data['description']
    
    if category is not None:
        validated_data = validate_product_data(product.name, product.price, product.description, category)
        product.category = validated_data['category']
    
    if stock is not None:
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError("Stock quantity cannot be negative")
            product.stock = stock
        except (TypeError, ValueError) as e:
            if "cannot be negative" in str(e):
                raise
            raise ValueError("Stock quantity must be a valid integer")
    
    product.updated_at = datetime.now()
    return product


def delete_product(product_id: str) -> bool:
    """
    Delete a product by its ID.
    
    Args:
        product_id (str): Product ID
    
    Returns:
        bool: True if product was deleted, False if not found
    """
    if not isinstance(product_id, str) or not product_id.strip():
        return False
    
    product_id = product_id.strip()
    if product_id in _products:
        del _products[product_id]
        return True
    
    return False


def update_stock(product_id: str, quantity: int) -> Optional[Product]:
    """
    Update product stock quantity.
    
    Args:
        product_id (str): Product ID
        quantity (int): New stock quantity
    
    Returns:
        Optional[Product]: Updated product or None if not found
    
    Raises:
        ValueError: If quantity is invalid
    """
    product = get_product(product_id)
    if not product:
        return None
    
    try:
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
        product.stock = quantity
        product.updated_at = datetime.now()
        return product
    except (TypeError, ValueError) as e:
        if "cannot be negative" in str(e):
            raise
        raise ValueError("Stock quantity must be a valid integer")


def adjust_stock(product_id: str, adjustment: int) -> Optional[Product]:
    """
    Adjust product stock by a given amount (positive or negative).
    
    Args:
        product_id (str): Product ID
        adjustment (int): Stock adjustment amount
    
    Returns:
        Optional[Product]: Updated product or None if not found
    
    Raises:
        ValueError: If adjustment would result in negative stock
    """
    product = get_product(product_id)
    if not product:
        return None
    
    try:
        adjustment = int(adjustment)
        new_stock = product.stock + adjustment
        if new_stock < 0:
            raise ValueError(f"Insufficient stock. Current: {product.stock}, Adjustment: {adjustment}")
        
        product.stock = new_stock
        product.updated_at = datetime.now()
        return product
    except (TypeError, ValueError) as e:
        if "Insufficient stock" in str(e):
            raise
        raise ValueError("Stock adjustment must be a valid integer")


def is_available(product_id: str, quantity: int = 1) -> bool:
    """
    Check if a product is available in the requested quantity.
    
    Args:
        product_id (str): Product ID
        quantity (int): Requested quantity
    
    Returns:
        bool: True if available, False otherwise
    """
    product = get_product(product_id)
    if not product:
        return False
    
    try:
        quantity = int(quantity)
        return product.stock >= quantity and quantity > 0
    except (TypeError, ValueError):
        return False


def get_low_stock_products(threshold: int = 10) -> List[Product]:
    """
    Get products with stock below the specified threshold.
    
    Args:
        threshold (int): Stock threshold
    
    Returns:
        List[Product]: Products with low stock
    """
    try:
        threshold = int(threshold)
        return [product for product in _products.values() if product.stock <= threshold]
    except (TypeError, ValueError):
        return []


def search_products(query: str, search_fields: List[str] = None) -> List[Product]:
    """
    Search products by name, description, or category.
    
    Args:
        query (str): Search query
        search_fields (List[str], optional): Fields to search in ['name', 'description', 'category']
    
    Returns:
        List[Product]: Matching products
    """
    if not isinstance(query, str) or not query.strip():
        return []
    
    if search_fields is None:
        search_fields = ['name', 'description', 'category']
    
    query = query.strip().lower()
    results = []
    
    for product in _products.values():
        match_found = False
        
        if 'name' in search_fields and query in product.name.lower():
            match_found = True
        elif 'description' in search_fields and query in product.description.lower():
            match_found = True
        elif 'category' in search_fields and query in product.category.lower():
            match_found = True
        
        if match_found:
            results.append(product)
    
    return results


def filter_by_category(category: str) -> List[Product]:
    """
    Filter products by category.
    
    Args:
        category (str): Category to filter by
    
    Returns:
        List[Product]: Products in the specified category
    """
    if not isinstance(category, str) or not category.strip():
        return []
    
    category = category.strip().lower()
    return [product for product in _products.values() if product.category.lower() == category]


def filter_by_price_range(min_price: Union[float, int, str] = None, 
                         max_price: Union[float, int, str] = None) -> List[Product]:
    """
    Filter products by price range.
    
    Args:
        min_price (Union[float, int, str], optional): Minimum price
        max_price (Union[float, int, str], optional): Maximum price
    
    Returns:
        List[Product]: Products within the specified price range
    """
    results = list(_products.values())
    
    if min_price is not None:
        try:
            min_price = float(min_price)
            results = [product for product in results if product.price >= min_price]
        except (TypeError, ValueError):
            return []
    
    if max_price is not None:
        try:
            max_price = float(max_price)
            results = [product for product in results if product.price <= max_price]
        except (TypeError, ValueError):
            return []
    
    return results


def get_all_products() -> List[Product]:
    """
    Get all products.
    
    Returns:
        List[Product]: All products
    """
    return list(_products.values())


def get_product_count() -> int:
    """
    Get the total number of products.
    
    Returns:
        int: Number of products
    """
    return len(_products)


def clear_all_products():
    """Clear all products from storage (useful for testing)."""
    global _products
    _products = {}