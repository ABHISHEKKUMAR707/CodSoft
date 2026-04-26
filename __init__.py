"""
Root package initialization for the Python project.

This file makes the project directory a proper Python package,
allowing for proper imports and package management.
"""

__version__ = "1.0.0"
__author__ = "Development Team"

# Import main modules for easier access
from . import hello

__all__ = ['hello']