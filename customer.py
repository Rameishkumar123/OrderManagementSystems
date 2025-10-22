"""
Customer class file

Step-by-step Instructions:
1. Define attributes:
   - customer_id (int)
   - name (str)
   - email (str)
   - orders (list of Order objects)
2. Add __init__, add_order, get_order_history methods.
Hint: Use a list to store order references.
"""

class Customer:
    """
    customer class contain attribute customer_id,name,email,orders
    """
    def __init__(self, customer_id, name, email):
        # TODO: Initialize attributes
        # Hint: self.orders = []
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []

    """
    we are not using this method. we did directly by append on orders in main function
    """
    def add_order(self, order):
        # TODO: Append order to list
        # Hint: self.orders.append(order)
        pass

    """
    we are not using this method. we printing in main function
    """
    def get_order_history(self):
        # TODO: Return order details
        # Hint: Loop through self.orders and return summaries
        pass

    def __str__(self):
        """
        this method is used to represent the Customer information
        """
        # return (f"Customer[{self.customer_id}]  {self.name} {self.email}," 
        #         f"orders={{{', '.join([f'{p.name} - {qty} - {o.status} ' for p,qty in o.products.items() for o in self.orders])}}} ")
        orders_str = ', '.join([
        f"Product Name:{p.name} - Price:{p.price} - Quantity:{qty}  - {o.status.name}"
        for o in self.orders
        for p, qty in o.products.items()
        ])
        return f"Customer[{self.customer_id}] {self.name} ({self.email}), orders={{ {orders_str} }}"