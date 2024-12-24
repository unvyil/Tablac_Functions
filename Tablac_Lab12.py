def menu_choices():
    # Define the menu items with names and prices
    menu = {
        1: ("Sisig", 90),
        2: ("Buttered Shrimp", 90),
        3: ("Chopsuey", 90),
        4: ("Liempo", 119)
    }
    print("\n ⋆｡‧˚ʚ Welcome to Vy's Food Kiosk (Online Payment only)! ɞ˚‧｡⋆ \n\nMenu:\n")
    # Display the menu with item names and prices
    for key, (name, price) in menu.items():
        print(f"{key}. {name} - ₱{price:.2f}")
    return menu

def order(menu):
    # Allow the user to choose a menu item
    while True:
        choice = input("\nEnter the menu number of your choice: ")
        if choice.isdigit() and int(choice) in menu:
            return menu[int(choice)]  # Return the selected item
        print("\nInvalid choice. Please try again.") 

def choose_payment_method():
    # Prompt the user to select a payment method
    while True:
        payment_method = input("\nSelect payment method (1 for GCash, 2 for PayMaya): ")
        if payment_method in ['1', '2']:
            if payment_method == '1':
                print("\nYou selected GCash.")
                return 'GCash'
            else:
                print("\nYou selected PayMaya.")
                return 'PayMaya'
        print("\nInvalid choice. Please select a valid payment method.") 

def get_payment_number(payment_method):
    # Request the user's payment number (GCash or PayMaya)
    while True:
        number = input(f"\nEnter your {payment_method} number: ")
        if number.isdigit():
            return number  # Return the payment number if valid
        print("\nInvalid number. Please try again.")

def payment(total_cost):
    # Process payment and check if sufficient funds are provided
    while True:
        cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Enter payment amount: ")
        if cash.replace('.', '', 1).isdigit():
            cash = float(cash)
            if cash >= total_cost:
                change = cash - total_cost  # Calculate change
                print(f"\nPayment accepted. Change: ₱{change:.2f}.")
                return change 
        print("\nInvalid or insufficient payment. Try again.") 

def main():
    orders = []  # List to store all orders
    total_amount = 0  # Total cost tracking variable
    while True:
        menu = menu_choices()  # Show menu
        item_name, item_price = order(menu)  # Get user's order
        orders.append((item_name, item_price))  # Add order to list
        total_amount += item_price  # Add item price to total amount
        print(f"\nYou selected {item_name}. Total so far: ₱{total_amount:.2f}.")  # Show current total of all items

        # Ask if user wants to continue ordering
        next_order = input("\nWould you like to order something else? (Enter number 5 for no more orders, any other key to continue): ")
        if next_order == '5':  # If user enters 5, stop ordering
            break

    payment_method = choose_payment_method() 
    payment_number = get_payment_number(payment_method) 

    change = payment(total_amount)  # Process payment and calculate change

    # Print the receipt
    print("\n⋆｡‧˚ʚ Printing Receipt... ɞ˚‧｡⋆\n")
    print(" ┌─────────────────────────────┐ ")
    print(" │       Vy's Food Kiosk       │ ")
    print(" │-----------------------------│ ")
    for item_name, item_price in orders:
    # Print each ordered item and its price
        print(f" │ Item: {item_name:<20}  │")
        print(f" │ Price: ₱{item_price:<19.2f} │")
        print(" │-----------------------------│")
    # Print total and change
    print(f" │ Total: ₱{total_amount:<19.2f} │")
    print(f" │ Change: ₱{change:<19.2f}│")
    print(" └─────────────────────────────┘")
    print("\nThank you for your order!") 

if __name__ == "__main__":
    main()