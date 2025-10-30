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
        self.orders = {}

    """
    adding order to customer
    """
    def add_order(self, order):
        # TODO: Append order to list
        self.orders[order.order_id] = order
        #pass

    """
    this method is used to get order history
    """
    def get_order_history(self):
        # TODO: Return order details
        # Hint: Loop through self.orders and return summaries
        if not self.orders:
            return f"Customer[{self.customer_id}] {self.name} ({self.email}), orders=No orders placed yet."
        #total = sum( q*p.price for p, q in self.orders.products.items())
        total = sum( q*p.price for o in self.orders.values() for p, q in o.products.items())
        print("total",total)
        
        orders_str = ', '.join([
        f"Product Name:{p.name} - Price:{p.price} - Quantity:{qty}  - {o.status.name}"
        for o in self.orders.values()
        for p, qty in o.products.items()
        ])
        return f"Customer[{self.customer_id}] {self.name} ({self.email}), orders={orders_str}, total Cost= {total}"
        

    def __str__(self):
        """
        this method is used to represent the Customer information
        """
        orders_str = ', '.join([
        f"Product Name:{p.name} - Price:{p.price} - Quantity:{qty}  - {o.status.name}"
        for o in self.orders.values()
        for p, qty in o.products.items()
        ])
        return f"Customer[{self.customer_id}] {self.name} ({self.email}), orders={{ {orders_str} }}"
