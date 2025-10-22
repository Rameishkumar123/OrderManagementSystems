"""
Order class file

Step-by-step Instructions:
1. Define attributes:
   - order_id (int)
   - customer (Customer object)
   - products (dict {Product: qty})
   - status (OrderStatus enum)
2. Add methods:
   - add_product(product, qty)
   - remove_product(product_id)
   - calculate_total()
   - update_status(new_status)
"""

from order_status import OrderStatus
from exceptions import *

class Order:
    """
    this Order class has attribute order_id,customer,products,status
    """
    def __init__(self, order_id, customer):
        # TODO: Initialize with empty products dict
        # Hint: self.products = {}
        self.order_id=order_id
        self.customer = customer
        self.products = {}
        self.status = OrderStatus.PENDING
        #pass

    """
    this method is used to add product to order
    """
    def add_product(self, product, qty):
        # TODO: Add product to dict
        # Hint: self.products[product] = self.products.get(product, 0) + qty
        self.products[product] = self.products.get(product, 0) + int(qty)
        #pass

    """
    this method is used to remove product from order
    """
    def remove_product(self, product_id):
        # TODO: Remove product from dict
        # Hint: loop through keys and match product.product_id
        for product in list(self.products.keys()):
            if product.product_id == product_id:
                print("product_id",product_id)
                del self.products[product]
                break

    """
    this method is used to calculate the total cost
    """
    def calculate_total(self):
        # TODO: Return total amount
        # Hint: Use sum(p.price * qty for p, qty in self.products.items())
        return sum(p.price * qty for p, qty in self.products.items())
        

    """
    this method is used to update the status of order
    """
    def update_status(self, new_status):
        # TODO: Update order status
        try:
            if isinstance(new_status, OrderStatus):
                self.status = new_status                    
            else:
                raise InvalidStatus("Invalid status. Must be an instance of OrderStatus.")
        except Exception as e:
                print("Error:", e)    


    """
    this method is used to represent the order data
    """
    def __repr__(self):
        return (f"Order(order_id={self.order_id}, "
                f"customer={self.customer.name if hasattr(self.customer, 'name') else self.customer}, "
                f"products={{{', '.join([f'product name {p.name}: quantity {q},price : {p.price}' for p, q in self.products.items()])}}}, "
                f"status={self.status.name})")
            
