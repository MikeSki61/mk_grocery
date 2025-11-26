import mk_core
print("Welcome to the brand new MK Grocery APP!")

def launch():
    while True:
        command = input("Enter a command(add, remove, edit, list, export, quit):")

        if command == "add":
            print("Here's where you add items to your grocery list.")
            name, store, cost, amount, priority, buy = get_inputs()
            mk_core.add_item(name=name, store=store, cost=cost, amount=amount, priority=priority, buy=buy)

        if command == "remove":
            print("Here's where you remove items from your grocery list.")
            name = input("Enter the item to remove: ")

            mk_core.remove_item(name)

        if command == "edit":
            print("This allows you to edit any item on yoiur shopping list.")
            name, store, cost, amount, priority, buy = get_inputs()

            mk_core.edit_item(name, store, cost, amount, priority, buy)

        if command == "list":
            print("This allows you to list the items in your shopping list")
            mk_core.list_items()

        if command == "export":
            print("Use this to export your shopping list.")
            mk_core.export_items()

        if command == "quit":
            print("This will quit the program")
            break

def get_inputs():
        while True:
            name = input("item name (ex. cheese): ")
            if name:
                break
            print("Invalid input. Please enter a valid item.")

        while True:
            store = input("What's te name of the store?: ")
            if store:
                break
            print("Invalid input. Please add a valid store name.")

        while True:
            try:
                cost = float(input("Item price (ex. 1.95): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid price")

        while True:
            try:
                amount = (input("Item quantity: "))
                if amount == "skip":
                    amount = None
                    break
                elif int(amount) > 0:
                    amount = int(amount)
                    break
                else:
                    print("Quantity mst bne a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid quantity")

        while True:
            try:
                priority = input("What's the items riority(i.e. 1 is the highest and 5 the lowest): ")
                if priority == "skip":
                    priority = None
                    break
                elif 1 <= int(priority) <= 5:
                    break
                else:
                    print("Priority must be between 1 and 5")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        while True:
            try:
                buy = input("Confirm you intend to buy the item:" )
                if buy.lower() == "true":
                    buy = True
                    break
                elif buy.lower() == "false":
                    buy = False
                    break
                elif buy == "skip":
                    buy == "skip"
                    break
                else:
                    print("Invalid input. Please enter true or flalse")
            except ValueError:
                print("Invalid input. Please enter'true' or 'false'")

        return name, store, cost, amount, priority, buy     

if __name__ == '__main__':
    launch()


