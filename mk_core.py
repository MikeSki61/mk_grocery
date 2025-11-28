
"""
mk_core.py
This file is the core file that provides the functions for the app.
It includes the ability to add, remove, edit, and export the list.

Functions are:
- add_items(): Add items to the list.
-remove_items(): Removes items from the list.
-edit_items(): Edits any item within the list. Any value can be edited.
-export_items(): Able to export the list.

Author: Mike Kwiatkowsky
Version:1.0.0
"""
# The grocery_list is a list of items showing the keywords and values of each.
# Also this shows the type of item within the list ex: "name" is a string,
# cost is a float, priority is an integer and buy is a boolean.-True or False.
grocery_list: list[dict[str, float | int | bool | str]] = [
    {
        "name": "milk",
        "store": "Walmart",
        "cost": 6.47,
        "amount": 2,
        "priority": 1,
        "buy": True,
    },
    {
        "name": "bread",
        "store": "Wal-Mart",
        "cost": 4.50,
        "amount": 2,
        "priority": 1,
        "buy": True,

    },
    {"name": "eggs",
        "store": "Wal-Mart",
        "cost": 5.0,
        "amount": 1,
        "priority": 1,
        "buy": True,
    },
    
]

# Function to add items to your grocery list
def add_item(
        name: str,
        store: str,
        cost: float,
        amount: int,
        priority:int,
        buy: bool
):
    """This is a function to add the arguments
    for the addition of an item to the list.

    Args:
        name (str): a string
        store (str): a string
        cost (float): a float
        amount (int): an integer
        priority (int): an integer
        buy (bool): a boolean
    """
    
    # Defined dictionary item to add to list
    item = {
        "name": name, 
        "store": store, 
        "cost": cost, 
        "amount": amount, 
        "priority": priority, 
        "buy": buy
    }
    # Defined dictionary item to add to list
    grocery_list.append(item)

#Remove item from grocery list
def remove_item(name):
    """This is a function to remove items
        from the list as a string.

    Args:
        name (str): string

    Returns:
        str: _return item as a string
    """

    #Use name key to identify item to remove
    index = get_index_from_name(name)
    #Remove item from the list
    grocery_list.pop(index)

#Edit list parameters
def edit_item(
    name, store= None, 
    cost= None, 
    amount= None, 
    priority= None,
    buy=None
):
    """This is  function the allows the user to edit the items in a list.

    Args:
        name (str): _a string
        store (str): _a string
        cost (float): _ a float
        amount (int): _an integer
        priority (int): _an integer_
        buy (bool): _a boolean
    """
    
    index = get_index_from_name(name)

    old_item = grocery_list[index]
    
    if not store:
        store = old_item["store"]

    if not cost:
        cost = old_item["cost"]

    if not amount:
        amount = old_item["amount"]

    if not priority:
        priority = old_item["priority"]

    if not buy:
        buy = old_item["buy"]

    item = {
        "name": name, 
        "store": store, 
        "cost": cost, 
        "amount": amount, 
        "priority": priority, 
        "buy": True
}

    grocery_list[index] = item
   
# Display item in a more readible format and display total
def export_items():
    buy_list = []
    """_The export_items() function will export the items that may have
been edited, removed or  added to the list, 
creating a new list called the buy_list.
    """

    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)

        if buy_list:
            for item in buy_list:
                print(
                f"name:{item['name']} -"
                f"store:{item['store']} -"
                f"cost: ${item['cost']} -"
                f"amount: {item['amount']} -"
                f"priority: {item['priority']}"
                )
            
        total_cost = calculate_total_cost(buy_list, round_cost = True)

        print(f"The total cost is ${total_cost}")


# Get index of the grocery item        
def get_index_from_name(name):
    index = 0
    """_The get_index_from_name(name) function 
will return the name of the item.

    Returns:
        _name_: _will return a string
    """

# Use loop to check if item name on list
    for item in grocery_list:
        if item ["name"] == name:  # If item is equal to name, returns the value.
            return index
        else:
            index += 1 # Adds the item increases the count by one.

# Display current grocery list
def list_items()-> str:
    """The list_items() function will list / print the items.

    Returns:
        str: -items as a string
    """
    for item in grocery_list:
        print(item)

# Define a global constant for the default tax rate
TAX = 0.8

# Calculate the total of your grocery list including sales tax in Virginia
def calculate_total_cost(grocery_list, round_cost = False):
    """_Parameters
    grocery_list (list[dict]): A list of dictionaries where each dictionary represents
                            an item with keys 'amount' (int) and 'cost' (float).
    round_cost (bool): If True, rounds the total cost to the nearest integer. Default is False.
    tax (float): The tax rate to apply to the total cost. Default is the global TAX constant.

    Returns:
        _float: The total cost after applying tax and optional rounding.
    """
    total_cost = 0
    # Calculate cost and add to total cost
    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    # Calculate total cost and tax, the round to nearest 100th of a cent
    if round_cost:
        total_cost = round(total_cost)
        
    if TAX:
        tax_cost = total_cost * TAX
        total_cost += tax_cost
    # total cost returned once all items in the grocery list are calculated for use in other defintions
    return total_cost

# export_items()












