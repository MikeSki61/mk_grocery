
import mk_core
print("Welcome to the brand new MK Grocery APP!")

def launch():
    while True:
        command = input("Enter a command(add, remove, edit, list, export, " \
        "quit):")

        if command == "add": # This will allow the user to add items.
            print("Here's where you add items to your grocery list.")
            name, store, cost, amount, priority, buy = get_inputs()
            mk_core.add_item(
                name=name, 
                store=store, 
                cost=cost, 
                amount=amount,
                priority=priority, 
                buy=buy
            )

            print(f"{name} added to list")

        if command == "remove":  # this is the command to remove an item.
            print("Here's where you remove items from your grocery list.")
            name = input("Enter the item to remove: ")

            mk_core.remove_item(name)

        if command == "edit": # This is the command to be used to edit
            # items in the list.
            print("This allows you to edit any item on yoiur shopping list.")
            name, store, cost, amount, priority, buy=get_inputs()
            index = mk_core.get_index_from_name(name)
            item = mk_core.grocery_list[index]
            id = item["id"]
            mk_core.edit_item(name, store, cost, amount, priority, buy, id)
            print(f"{name} was edited.")


        if command == "list":
            # This command will list the items
            # selected in the list from the core module.
            print("This allows you to list the items in your shopping list")
            mk_core.list_items()

        if command == "export":
            print("Use this to export your shopping list.")
            mk_core.export_items()

        if command == "quit":
            print("This will quit the program")
            break

def get_inputs():
        """The following functions are for the inputs
    to collect information for the list.
export

        Returns:
            string:  item to be added as a string
    """
        while True:
            name = input("item name (ex. cheese): ")
            if name:
                break
            print("Invalid input. Please enter a valid item.")

        while True: # this input will alert the user that
        # there is no valid entry if the option is skipped.
            store = input("What's the name of the store?: ")
            if store:
                break
            print("Invalid input. Please add a valid store name.")

        while True: # this input will alert the user that
        # there is no valid entry if the option is skipped
            try:
                cost = float(input("Item price (ex. 1.95): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid price")

        while True: # this input will alert the user that
        # there is no valid entry if the option is skipped.
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

        while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
            try:
                priority = input("What's the items riority(i.e. 1 is the " \
                "highest and 5 the lowest): ")
                if priority == "skip":
                    priority = None
                    break
                elif 1 <= int(priority) <= 5:
                    break
                else:
                    print("Priority must be between 1 and 5")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        while True: # this input will alert the user that
        # there is no valid entry if the option is skipped.
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

# Call the function
if __name__ == '__main__':
    launch()


