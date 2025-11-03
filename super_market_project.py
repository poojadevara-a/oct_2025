# Build a Python-based supermarket billing system that allows users to view a list of products, add items to their cart, calculate the total bill with tax, and display a receipt.
# Functional Requirements:

# Functional Requirements:
    # The system should ask for the customer’s name.
    # Display a list of available products with their prices.
    # Allow users to add multiple items to their cart.
    # Validate that the quantity entered is a valid number.

# Product Catalog:
    # Maintain a dictionary of products and their prices.
    # Display the product list when requested.

# Billing and Calculations:
    # Compute the total price based on item quantities.
    # Apply a 12% tax on the total amount.
    # Display a detailed invoice with:
        # Item name
        # Quantity
        # Price per unit
        # Total price for each item
        # Total amount before and after tax

# Receipt Format:
    # Display a well-formatted bill with store name, location, and transaction details.

# Exit Mechanism:
    # Allow users to exit the purchase process at any time.
    # Display a "Thank you" message upon exiting.




#List of items
lists = """
Rice        Rs.15/kg
Diary Milk  Rs.10/item
Sugar       Rs.10/kg
Oil         Rs.30/liter
Salt        Rs.30/pack
Paneer      Rs.150/Kg
Maggie      Rs.20/pack
Boost       Rs.200/bottle
Water       Rs.10/bottle
Biscuit     Rs.20/pack
"""
SNo = 0
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
price_list = []
quantity_list = []

name = input("Enter your Name: ")

Items = {"Rice": 15, "Diary Milk": 10, "Sugar": 10, "Oil": 30, "Salt": 30, "Paneer": 150, "Maggie": 20, "Boost": 200, "Water": 10, "Biscuit": 20}
item_list = []

while True:
    choice = input("Press 1 for List of items or Press 2 to Exit: ")
    if choice == "2":
        print("Thank you for shopping with us!")
        break
    elif choice =="1":
        print(f"Items available: \n{Items}")

        while True:
            input1 = input("To buy press 1 or press 2 to exit: ")
            if input1 == "2":
                print("Thank you for shopping with us!")
                break
            if input1 == "1":
                items_in_cart = input("Enter the Item to add to cart: ").title()
                while True:
                    quantity_of_item = (input("Enter the Quantity: "))
                    if quantity_of_item.isdigit():
                        quantity = int(quantity_of_item)
                        break
                    else:
                        print("Please enter the valid quantity: ")
            if items_in_cart in Items:
                price = quantity * Items[items_in_cart]
                pricelist.append((items_in_cart, quantity_of_item, Items[items_in_cart],price))
                totalprice += price
                item_list.append(items_in_cart)
                quantity_list.append(quantity)
                price_list.append(totalprice)
                tax = (totalprice*18)/100
                Finalprice = totalprice+tax
                # print("Finalprice")
            else:
                print("Please enter the valid input.")
        
        print(" ")
        print("\t\tPython Super Market Bill System")
        print(" ")
        print("\t\tLocation - Hyderabad")
        print("-"*60)
        print("-"*60)
        print("Name -", name)
        #imporetd date and time
        from datetime import datetime
        current_date_time = datetime.now()
        print("Date and Time: ", current_date_time)
        print("-"*60)
        print("SNo \titems \tquantity \t\t\tprice")
        for i, j, k, l in pricelist:
            SNo+=1
            print(f"{SNo}\t{i}\t{j}\t\t\t\t{l}")
        print("-"*60)
        print(f"\t\t\t\tTotal Amount:Rs.{totalprice}")
        print(f"Tax amount:{" "*35} {tax}")
        print("-"*60)
        print(f"{" "*32} Final Amount: {Finalprice}")
        print("-"*60)
        print("\t\t Thank you & Visit again")
        print("-"*60)


        




        
        









            



































































































































