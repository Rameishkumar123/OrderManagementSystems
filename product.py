"""
Product class file

Step-by-step Instructions:
1. Define attributes:
   - product_id (int)
   - name (str)
   - price (float)
   - stock (int)
2. Add __init__, __str__, and update_stock methods.
3. Ensure stock >= 0 and price >= 0.
Hint: Use `max(0, stock)` to avoid negative stock values.
"""

class Product:
    """
    This Product class has attribute product_id, name, price, stock
    """
    def __init__(self, product_id, name, price, stock):
        # TODO: Initialize attributes
        # Hint: validate that price >= 0 and stock >= 0
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock


    """
    This method is used to represent the Product Information
    """
    def __str__(self):
        # TODO: Return formatted string
        # Hint: f"Product[{self.product_id}] {self.name} - ${self.price}, Stock: {self.stock}"
        return f"Product[{self.product_id}] {self.name} - ${self.price}, Stock: {self.stock}"
        
    """
    This method is used to add stock to product
    """    
    def update_stock(self, quantity):
        # TODO: Increase or decrease stock
        # Hint: self.stock += quantity (but ensure it doesn't go below 0)
        self.stock += quantity

    """
    This method is used to remove stock from product
    """
    def remove_stock(self, quantity):
        # TODO: Increase or decrease stock
        # Hint: self.stock += quantity (but ensure it doesn't go below 0)
        self.stock -= quantity            
