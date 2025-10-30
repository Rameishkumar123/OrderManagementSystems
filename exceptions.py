"""
Custom exceptions for order management
"""

class OutOfStockError(Exception):
    """Raised when product stock is insufficient"""
    pass

class InvalidOrderOperationError(Exception):
    """Raised for invalid order operations"""
    pass

class CustomerNotFoundError(Exception):
    """Raised when customer is not found"""
    pass

class ProductNotFoundError(Exception):
    """Raised when product is not found"""
    pass

class ProductAlreadyExistsError(Exception):
    """Raised when product is not found"""
    pass

class OrderNotFoundError(Exception):
    """Raised when product is not found"""
    pass

class InvalidStatus(Exception):
    """Raised when product is not found"""
    pass

