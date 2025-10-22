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

class Report:
    def order_summary(self, order):
        # TODO: Print products and total
        # Hint: loop order.products and calculate total
        pass

    def customer_orders(self, customer):
        # TODO: Show all orders by a customer
        # Hint: use customer.get_order_history()
        pass

    def sales_report(self, orders):
        # TODO: Generate total sales
        # Hint: sum(order.calculate_total() for order in orders)
        pass
