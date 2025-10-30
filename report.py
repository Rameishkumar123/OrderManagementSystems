"""
Report class file

Step-by-step Instructions:
1. Add methods:
   - order_summary(order)
   - customer_orders(customer)
   - sales_report(orders)
2. Display clean formatted output.
Hint: Use loops and f-strings to format reports.
"""

"""
Reports class for generating reports
"""
class Report:

    """
    order_summary method to show order details for a given order
    """
    def order_summary(self, order):
        # TODO: Print products and total
        # Hint: loop order.products and calculate total
        
        #for oid,order in  orders.items():
                #    print(order)
        total = sum( q*p.price for p, q in order.products.items())
        return (f"Order(order_id={order.order_id}, "
                f"customer={order.customer.name if hasattr(order.customer, 'name') else order.customer}, "
                f"products={{{', '.join([f'product name {p.name}: quantity {q},price : {p.price}' for p, q in order.products.items()])}}}, "
                f"status={order.status.name}),"
                f"Total Cost={total}),")        

    """
    method to show all orders by a customer
    """
    def customer_orders(self, customer):
        # TODO: Show all orders by a customer
        # Hint: use customer.get_order_history()
        result = customer.get_order_history()
        return result

    """
    method to show total sales from all orders
    """        
    def sales_report(self, orders):
        # TODO: Generate total sales
        # Hint: 
        total = sum(order.calculate_total() for order in orders)
        return total
        #pass
