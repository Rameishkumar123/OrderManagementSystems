"""
Main driver file


Step-by-step Instructions:
1. Import Product, Customer, Order, Report, etc.
2. Create sample customers and products.
3. Show menu:
   a. Create order
   b. Add product to order
   c. Remove product
   d. View order summary
   e. Customer order history
   f. Add Customers
   g. Add products
   h. Add stocks to products
   i. Exit
4. Handle invalid input with try/except.
Hint: Use while True loop with input() for menu.
"""

from customer import Customer
from product import Product
from order import Order
from report import Report
from exceptions import *
from order_status import OrderStatus
from utils import *
from report import *

def main():
    """
    This Main will add customer,order,product.Give Reports also
    """
    # TODO: Implement menu-driven logic here
    # Hint: Keep customers and orders in lists/dictionaries
    customers = {}
    products = {}
    orders = {}
    while True:
        print("a. Add Customers")
        print("b. Add products")
        print("c. Create order")
        print("d. Add product to order")
        print("e. Remove product to order")
        print("f. View order summary")
        print("g. View Customer order summary")
        print("h. Add stocks to products")
        print("i. Update status to order")
        print("j. calculate Total for order")
        print("k. View order summary")
        print("l. Exit")
        #print("m. Exit")
        choice = input("Enter choice: ")

        if choice == "a": # Add Customers
            print("Add Customers")
            cid = input("Customer ID: ")
            name = input("Name: ")
            email = input("Email: ")

            customer_object = Customer(cid, name, email)
            customers[cid] = customer_object
            print("Customer added.")

        elif choice == "b": # Add products
            try:
                print("Add products")
                pid = input("Product ID: ")
                name = input("Name: ")
                price = int(input("Price: "))
                stock = int(input("Stock: "))
                
                if pid in products:
                    raise ProductAlreadyExistsError("Product with this ID already exists.")
                price = validate_price(price)
                stock = validate_quantity(stock)
                product_object = Product(pid, name, price, stock)
                products[pid] = product_object
                print("product added.")
            except Exception as e:
                print("Error: ",e)            

        elif choice == "c": # create an order
            print("Create order")
            oid = input("Order ID: ")
            cid = input("Customer Id: ")
            
            try:
                if cid not in customers:
                        raise CustomerNotFoundError("Customer not found")

                customer = customers[cid]    
                orders[oid] = Order(oid,customer)
                print("order placed")
            except Exception as e:
                print("Error:", e)    

        elif choice == "d": # Add product to order
            print("Add product to order")
            oid = input("Order ID: ")
            pid = input("Product Id: ")
            qty = input("quantity: ")
            try:
                if oid not in orders:
                    raise OrderNotFoundError("Order not found")
                
                if pid not in products:
                    raise ProductNotFoundError("Product not found")

                order = orders[oid]
                customer = order.customer
                
                product = products[pid]
                order.add_product(product,qty)   
                customer.add_order(order)
                product.remove_stock(int(qty))   
                print("product added")         
                   
            except Exception as e:
                print("Error:", e) 

        elif choice == "e": # Remove product to order
            print("Remove product to order")
            oid = input("Order ID: ")
            pid = input("Product Id: ")     
            try:
                if oid not in orders:
                    raise OrderNotFoundError("Order not found")
                
                if pid not in products:
                    raise ProductNotFoundError("Product not found")

                order = orders[oid]
                product = products[pid]
                qty = int(order.products[product])
                order.remove_product(pid)                  
                print("order.products[product]",order.products)
                product.update_stock(qty)             
                print("product removed")   
            except Exception as e:
                print("Error:", e)
        
        elif choice == "f": # View Particular order summary
            print("for Particular Order summary")
            try:
                oid = input("Order ID for order summary: ")
                if oid not in orders:
                    raise OrderNotFoundError("Order not found")
                
                order = orders[oid]
                report = Report()
                result = report.order_summary(order)
                print("Order list")
                print(result)
                   
            except Exception as e:
                print("Error:", e)

        elif choice == "g": # View Customer order summary
            try:
                print("for Customer order Summary")
                cid = input("Customer Id: ")
                if cid not in customers:
                        raise CustomerNotFoundError("Customer not found")
                
                customer = customers[cid]
                report = Report()
                result = report.customer_orders(customer)
                print("Customer order Summary")
                print(result)
                
            except Exception as e:
                print("Error:", e)        

        elif choice == "h": # Add stocks to products
            print("Add stocks to products")
            pid = input("Enter Product Id: ")
            qty = input("Enter New Stock Quantity: ")
            try:
                if pid not in products:
                    raise ProductNotFoundError("Product not found")
                
                product = products[pid]
                product.update_stock(qty)
                print("quantity of product Updated.")
            except Exception as e:
                print("Error:", e)

        elif choice == "i": # Update status to order
            print("Update status to order")
            oid = input("Order ID: ")
            status = input("Order Status Pending/Shipped/Delivered/Cancelled: ")
            try:
                if oid not in orders:
                    raise OrderNotFoundError("Order not found")
                
                order = orders[oid]
                if status == 'Delivered':
                    st= OrderStatus.DELIVERED
                elif status == 'Pending':
                    st= OrderStatus.PENDING
                elif status == 'Shipped':
                    st= OrderStatus.SHIPPED
                elif status == 'Cancelled':
                    st= OrderStatus.CANCELLED            
                order.update_status(st)
            except Exception as e:
                print("Error:", e)                           
                    
        elif choice == "j": # calculate Total for order
            oid = input("Order ID: ")
            #pid = input("Product Id: ")     
            try:
                if oid not in orders:
                    raise OrderNotFoundError("Order not found")
                
                #if pid not in products:
                #    raise ProductNotFoundError("Product not found")

                order = orders[oid]
                #product = products[pid]
                sum = order.calculate_total()
                print(f"sum is {sum}")  
            except Exception as e:
                print("Error:", e)    

        elif choice == "k": # View Total order summary
            try:
                print("View Total order summary")
                report = Report()
                total_sales = report.sales_report(orders.values())
                print(f"Total Sales: {total_sales}")
                print("product list")   
            except Exception as e:
                print("Error:", e)

        elif choice == "l": # exit
            print("Exiting...")
            break

        else:
            print("Invalid choice.")                

if __name__ == "__main__":
    main()
