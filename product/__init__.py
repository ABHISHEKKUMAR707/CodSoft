"""
Product management module.

This module provides comprehensive product management functionality including:
- Product creation, retrieval, updating, and deletion
- Inventory management with stock tracking
- Product validation and data formatting
- Search and filtering capabilities
"""

from .product import (
    Product,
    create_product,
    get_product,
    update_product,
    delete_product,
    validate_product_data,
    format_price,
    update_stock,
    adjust_stock,
    is_available,
    get_low_stock_products,
    search_products,
    filter_by_category,
    filter_by_price_range,
    get_all_products,
    get_product_count,
    clear_all_products
)

__all__ = [
    'Product',
    'create_product',
    'get_product',
    'update_product',
    'delete_product',
    'validate_product_data',
    'format_price',
    'update_stock',
    'adjust_stock',
    'is_available',
    'get_low_stock_products',
    'search_products',
    'filter_by_category',
    'filter_by_price_range',
    'get_all_products',
    'get_product_count',
    'clear_all_products'
]