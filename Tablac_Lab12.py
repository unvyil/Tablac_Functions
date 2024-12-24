def menu_choices():
    menu = {
        1: ("Sisig", 90),
        2: ("Buttered Shrimp", 90),
        3: ("Chopsuey", 90),
        4: ("Liempo", 119)
    }
    print("\n ⋆｡‧˚ʚ Welcome to Vy's Food Kiosk (Online Payment only)! ɞ˚‧｡⋆ \n\nMenu:\n")
    for key, (name, price) in menu.items():
        print(f"{key}. {name} - ₱{price:.2f}")
    return menu

def order(menu):
    while True:
        choice = input("\nEnter the menu number of your choice: ")
        if choice.isdigit() and int(choice) in menu:
            return menu[int(choice)]
        print("\nInvalid choice. Please try again.")

def choose_payment_method():
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
    while True:
        number = input(f"\nEnter your {payment_method} number: ")
        if number.isdigit():
            return number
        print("\nInvalid number. Please try again.")

def payment(total_cost):
    while True:
        cash = input(f"\nThe total cost is ₱{total_cost:.2f}. Enter payment amount: ")
        if cash.replace('.', '', 1).isdigit():
            cash = float(cash)
            if cash >= total_cost:
                change = cash - total_cost
                print(f"\nPayment accepted. Change: ₱{change:.2f}.")
                return change
        print("\nInvalid or insufficient payment. Try again.")

def main():
    orders = []
    total_amount = 0
    while True:
        menu = menu_choices()
        item_name, item_price = order(menu)
        orders.append((item_name, item_price))
        total_amount += item_price
        print(f"\nYou selected {item_name}. Total so far: ₱{total_amount:.2f}.")

        next_order = input("\nWould you like to order something else? (Enter number 5 for no more orders, any other key to continue): ")
        if next_order == '5':
            break

    payment_method = choose_payment_method()
    payment_number = get_payment_number(payment_method)

    change = payment(total_amount)

    print("\n⋆｡‧˚ʚ Printing Receipt... ɞ˚‧｡⋆\n")
    print(" ┌─────────────────────────────┐ ")
    print(" │       Vy's Food Kiosk       │ ")
    print(" │-----------------------------│ ")
    for item_name, item_price in orders:
        print(f" │ Item: {item_name:<20}  │")
        print(f" │ Price: ₱{item_price:<19.2f} │")
        print(" │-----------------------------│")
    print(f" │ Total: ₱{total_amount:<19.2f} │")
    print(f" │ Change: ₱{change:<19.2f}│")
    print(" └─────────────────────────────┘")
    print("\nThank you for your order!")

if __name__ == "__main__":
    main()