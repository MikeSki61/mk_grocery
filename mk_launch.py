
import mk_core
print("Welcome to the brand new MK Grocery APP!")




def launch():
    while True:
        command = input("Enter a command(add, remove, edit, list, export, " \
        "quit, search):")

        if command == "add":
            handle_add_command()


        if command == "remove":

            handle_remove_command()

        if command == "edit":

            handle_edit_command()

        if command == "list":
            print("This allows you to list the items in your shopping list")
            mk_core.list_items()

        if command == "export":
            print("Use this to export your shopping list.")
            mk_core.export_items()

        if command == "search":
            search_keyword = input("What is the name of the item" \
            " you would like to search? ")
            item = mk_core.search_item_name(search_keyword)

            if item:
                print(f"These items match your search: {item}")
            else:
                print(f"No items match the search ")

        if command == "quit":
            print("This will quit the program")
            break

def handle_add_command(): # This will allow the user to add items.
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
            
def handle_remove_command():  # this is the command to remove an item.
            #
        name = input("Which item would you like to remove? ")
        matches = mk_core.search_item_name(name)

        if not matches:
            print(f"I\'m sorry, I could not find a match for {name}")

        elif len(matches) > 1:
            for match_num, match in enumerate(matches, start =1):
                match_string = (
                    f"{match_num}. "
                    f"| Name: {match["name"]} "
                    f"| Store: {match["store"]} "
                    f"| Cost: {match["cost"]} "
                    f"| Amount: {match["amount"]} "
                    f"| Priority: {match["priority"]} "
                    f"| Buy: {match["buy"]} |" 
                )
                print(match_string)

            item_num = input('\nPlease select the number you would like to remove: ')
            match_item = matches[int(item_num) - 1]
            mk_core.remove_item(id=match_item['id'])
            print(f'\nItem {match_num} has been removed.')

        else:
            match_item = matches[0]
            mk_core.remove_item(id=match_item["id"])
            print(f"That item has been removed")

def handle_edit_command(): # This is the command to be used to edit
        target_item = input("Which item would you like to edit? ")
        matches = mk_core.search_item_name(target_item)

        if not matches:
            print(f"There are no items twith the name{target_item}")

        elif len(matches) > 1:
            match_num = 1
            for match in matches:
                match_string = (
                    f"item {match_num} "
                    f"| name: {match["name"]} "
                    f"| store: {match["store"]} "
                    f"| cost: {match["cost"]} "
                    f"| amount: {match["amount"]} "
                    f"| priority: {match["priority"]} "
                    f"| buy: {match["buy"]}"
                )
                print(match_string)
                match_num += 1

            item_num = input(
                "Which item do you want to edit?"
                )
            match_item = matches[int(item_num) - 1]
            name, store, cost, amount, priority, buy=get_inputs()
            mk_core.edit_item(
                 name, 
                 store, 
                 cost, 
                 amount, 
                 priority, 
                 buy, 
                 id=match_item["id"])
        else:
            match_item = matches[0]
            name, store, cost, amount, priority, buy=get_inputs()
            mk_core.edit_item(
                name, 
                 store, 
                 cost, 
                 amount, 
                 priority, 
                 buy, 
                 id=match_item["id"])

            print(f"{name} was edited.")
                
       

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


