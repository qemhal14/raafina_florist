from tabulate import tabulate
import json

# Function to read database
def readfile():
    with open('./Flower_inventory.json', 'r') as invent:
        table_flower = json.load(invent)
        return table_flower
table_flower = readfile()

# Function to changes database
def savefile():
    with open('./Flower_inventory.json', 'w') as invent:
        json.dump(table_flower, invent)

# Function to show table with index
def table():
    table= []
    for i, row in enumerate(table_flower[1:], start=1):
        indexed_row = [i] + row
        table.append(indexed_row)
    print(tabulate(table, headers=table_flower[0]))

# Function for user input and the available options
def user_inp(prompt, options):
    user_input = input(prompt)
    while user_input not in options:
        print("Invalid input!")
        user_input = input(prompt)
    return user_input

# Function for user input if input datatype
def user_inp_data(prompt, datatype):
    while True:
        try:
            user_input = input(prompt, datatype)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    return user_input

# Function to calculate the total inventory in the database
def total_invent():
    flower_count = len(table_flower) - 1
    return flower_count

# Function to display error message
def error_message():    
    print("Invalid input!")

# The main sort table function
def sort_table(table, options):
    if options == "category":
        sorted_table = sorted(table[1:], key=lambda x: x[1])
    elif options == "price":
        sorted_table = sorted(table[1:], key=lambda x: x[3])
    else:
        raise ValueError("Invalid sort option. Please choose 'category' or 'price'.")
    return sorted_table

# Function to sort by category
def sort_category():
    sorted_table_by_category = sort_table(table_flower, "category")
    print(tabulate(sorted_table_by_category, headers=table_flower[0]))

# Function to sort by price
def sort_price():
    sorted_table_by_price = sort_table(table_flower, "price")
    print(tabulate(sorted_table_by_price, headers=table_flower[0]))

# The options in price list
def menu_options():
    print(
    '''
        
    Menu options :
    1. Sort by category
    2. Sort by price
    3. Order a Flower
    4. Back to main menu
        ''')

# Program in the price list options
def menu():
    table()
    while True:
        menu_options()
        input_1 = user_inp("Input a menu you want to run (1/2/3/4):", ["1", "2", "3", "4"])
        if input_1 == "1":
            sort_category()
            continue
        elif input_1 == "2":
            sort_price()
            continue
        elif input_1 == "3":
            order()
            break
        elif input_1 == "4":
            break

# Function to update if flower exists
def update_existing_flower(input_name):
    for flower in table_flower:
        if input_name == flower[0].lower():
            while True:
                try:
                    stock_update = int(input("Enter stock: "))
                    if stock_update < 0:
                        error_message()
                        continue
                    break
                except ValueError:
                    error_message()
                    continue
            while True:
                try:
                    price_update = int(input("Enter price: "))
                    if price_update < 0:
                        error_message()
                        continue
                    break
                except ValueError:
                    error_message()
                    continue
            flower[2] += stock_update
            flower[3] = price_update
            savefile()
            print(f"Flower/leaves {input_name.title()} updated!")

# Function to add new item           
def new_flower(input_name):
    input_cat = user_inp("Enter category :", ["flower", "leaves"])
    while True:
        try:
            input_stock = int(input("Enter stock :"))
            if input_stock < 0:
                error_message()
                continue
            break
        except ValueError:
            error_message()
            continue
    while True:    
        try:
            input_price = int(input("Enter price :"))
            if input_price < 0:
                error_message()
                continue
            break
        except ValueError:
            error_message()
            continue
    invent_update = [input_name.title(), input_cat.capitalize(), input_stock, input_price]
    table_flower.append(invent_update)
    savefile()
    print("New flower/leaves added!")

# Main program for add/update stock
def update_flower():
    inp2_choice = user_inp("Do you want to 1. Add new  2. Cancel (1/2) :", ["1", "2"])
    if inp2_choice == "1":
        try:
            input_name = input("Enter flower/leaves name :").lower()
            while not input_name.isalpha():
                error_message()
                input_name = input("Enter flower/leaves name :").lower()
        except ValueError:
                error_message()
        flower_exists = False
        for flower in table_flower:
            if input_name == flower[0].lower():
                print(f"Flower/leaves {input_name.title()} already exists!")
                while True:
                    update_input = user_inp("Do you want to update stock instead? (yes/no) :", ["yes", "no"]).lower()
                    if update_input == "yes":
                        update_existing_flower(input_name)
                        flower_exists = True
                        break
                    elif update_input == "no":
                        flower_exists = True
                        break
        if not flower_exists:
            new_flower(input_name)
    elif inp2_choice == "2":
            print("Update canceled!")

# Function to delete
def delete(input_del):
    del table_flower[input_del]
    savefile()
    print("Flower/leaves successfuly deleted!")

# Main program in delete stock
def delete_flower():
    while True:
        choice_3 = user_inp("Do you want to proceed with the flower/leaves deletion ? (yes/no) :", ["yes", "no"])
        if choice_3 == "yes":
            total_invent()
            while True:
                table()
                try:
                    input_del = int(input("Enter flower/leaves index you want to delete :"))
                    if input_del > total_invent() or input_del <= 0:
                        error_message()
                        continue
                    else:
                        break
                except ValueError:
                    error_message()
        else:
            break
        flower_name = table_flower[input_del][0]
        confirm_inp = user_inp(f"Are you sure you want to delete flower/leaves {flower_name} from inventory ? (yes/no) :", ["yes", "no"])

        if confirm_inp == "yes":
            delete(input_del)
            
        elif confirm_inp == "no" or choice_3 == "no":
            print("Delete action canceled!")
            break

# Choices of product
def product_choice():
    print(
    '''
    Choose arrangement you want:
    1. Hand Bouquet
    2. Bloom Box
    3. Vase Arrangement
    4. Just Flower Please
    ''')

# Function to get product that user choice
def get_product_name():
    product_input = user_inp("Select product (1/2/3/4):", ["1", "2", "3", "4"])
    if product_input == "1":
        return "Hand Bouquet"
    elif product_input == "2":
        return "Bloom Box"
    elif product_input == "3":
        return "Vase Arrangement"
    elif product_input == "4":
        return "Just Flower Please"

# The price for each product options
def product_price(product_input):
    if product_input == "Hand Bouquet":
        return 50000
    elif product_input == "Bloom Box":
        return 120000
    elif product_input == "Vase Arrangement":
        return 150000
    elif product_input == "Just Flower Please":
        return 5000

# Choices of delivery location  
def delivery_location():
    print(
    '''
    Choose city you want the flower delivered to:
    1. Jakarta
    2. Bogor
    3. Depok
    4. Tanggerang
    5. Bekasi
    ''')

# Function to get the name of the delivery selected
def get_delivery_name():
    delivery_input = user_inp("Select location (1/2/3/4/5):", ["1", "2", "3", "4", "5"])
    if delivery_input == "1":
        return "Jakarta Delivery"
    elif delivery_input == "2":
        return "Bogor Delivery"
    elif delivery_input == "3":
        return "Depok Delivery"
    elif delivery_input == "4":
        return "Tanggerang Delivery"
    elif delivery_input == "5":
        return "Bekasi Delivery"

# The delivery price for each cities
def delivery_price(delivery_input):
    if delivery_input == "Jakarta Delivery":
        return 50000
    elif delivery_input == "Bogor Delivery":
        return 20000
    elif delivery_input == "Depok Delivery":
        return 30000
    elif delivery_input == "Tanggerang Delivery":
        return 80000
    elif delivery_input == "Bekasi Delivery":
        return 45000

# Function that return if customer get a cashback   
def cashback_message():
    print("Your order is above Rp 500000, you get 10% Cashback!")
    print("Apply 'GET10CB' below for the Cashback!")

# Function to calculate total amount in the cart
def calculate_total_price(cart):
    total_price = sum(row[2] for row in cart[1:])
    return total_price

# Function to display the cart and the sum of the total price 
def display_order_summary(cart, total_price):
    print(tabulate(cart))
    print("Here is the sum of your order:", total_price)

# Function for cashback voucher
def process_order(total_price):
    if total_price > 500000:
        cashback_message()
        voucher = user_inp("Enter code here: ","GET10CB")
        if voucher == "GET10CB":
            total_price *= 0.9
            print("Here is the sum of your order after Cashback:", total_price)
    return total_price

# Payment function
def get_payment(total_price):
    while True:
        try:
            payment = int(input("Enter money: "))
            if payment < total_price:
                print("Transaction cannot continue, your money is not enough!")
                print("Your money is short", total_price - payment)
            else:
                change = payment - total_price
                if change > 0:
                    print(change, "is your change.")
                print("Thank you for ordering, please wait while we prepare your order :)")
                break
        except ValueError:
            error_message()

# Function to update the stock in database after ordering
def update_stock(cart):
    for item in cart[1:]:
        flower_name = item[0]
        for i, row in enumerate(table_flower):
            if row[0] == flower_name:
                table_flower[i][2] -= item[1]
                break
    savefile()

# main program in order options
def order():
    total_invent()
    cart = [["Item", "Quantity", "Price"]]
    while True:
        table()
        try:
            continue_inp = user_inp("Continue order a flower? (yes/no) :", ["yes", "no"])
            if continue_inp == "yes":
                input_buy = int(input("Enter flower/leaves index you want to order: "))
                if input_buy < 0 or input_buy > total_invent():
                    error_message()
                    continue
                item_ordered = table_flower[input_buy]
                flower = item_ordered[0]
                stock = item_ordered[2]
                price = item_ordered[3]
            elif continue_inp == "no":
                break
        except ValueError:
            error_message()
            continue

        existing_index = None
        for i, item in enumerate(cart):
            if item[0] == flower:
                existing_index = i
                break

        while True:
            try:
                input_qty = int(input("Enter quantity: "))
                if input_qty <= stock and existing_index is not None:
                    cart[existing_index][1] += input_qty
                    break
                elif input_qty <= stock:
                    break
                print(f"{flower} stock is not enough! Stock remaining: {stock}.")
            except ValueError:
                error_message()
                continue
        subtotal_price = input_qty * price
        cart_update = [flower, input_qty, subtotal_price]
        if existing_index is None:
            cart.append(cart_update)
        print(tabulate(cart))

        add_another = user_inp("Do you like to add another flower/leaves? (yes/no): ", ["yes", "no"]).lower()
        if add_another == "no":
            product_choice()
            product_name = get_product_name()
            prod_price = product_price(product_name)
            product_cart = [product_name, 1, prod_price]  
            cart.append(product_cart)
            print(tabulate(cart))

            delivery_location()
            delivery_name = get_delivery_name()
            deli_price = delivery_price(delivery_name)
            delivery_cart = [delivery_name, 1, deli_price] 
            cart.append(delivery_cart)

            total_price = calculate_total_price(cart)
            display_order_summary(cart, total_price)
            total_price = process_order(total_price)
            get_payment(total_price)
            update_stock(cart)
            break

# Welcome function depending on role
def welcome(user):
    if user == "owner":
        print("Welcome Owner, Let's Spread Some Happiness!")
    elif user == "customer":
        print("Welcome, We Here to Bloom Your Day!")

# The main interface
def menu_interface():
    
    print('''
    Welcome to Raafina Bunga
          
    1. Our Price List
    2. Add/Update Stock
    3. Delete Stock
    4. Order a Flower
    5. Exit
    ''')

# The main program
def main():
    user = user_inp("Dou you want to continue as (owner/customer) :", ["owner", "customer"]).lower()
    user_login = False
    if user == "owner":
        user_inp("Please enter password :", ["admin"])
        user_login = True
    elif user == "customer":
        user_login = True

    while user_login == True:
        welcome(user)
        menu_interface()
        menu_inp = user_inp("Enter a menu you want to run :", ["1", "2", "3", "4", "5"])
        if menu_inp == "1":
            menu()
        elif menu_inp == "2" and user == "owner":
            update_flower()
        elif menu_inp == "2" and user == "customer":
            print("Sorry this feature only available for owner")
        elif menu_inp == "3" and user == "owner":
            delete_flower()
        elif menu_inp == "3" and user == "customer":
            print("Sorry this feature only available for owner")
        elif menu_inp == "4":
            order()
        elif menu_inp == "5":
            print("Thank You, Have a Blooming Day!")
            break

if __name__ == "__main__":
    main()