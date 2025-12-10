
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
Version:1.2.0
"""
# The grocery_list is a list of items showing the keywords and values of each.
# Also this shows the type of item within the list ex: "name" is a string,
# cost is a float, priority is an integer and buy is a boolean.-True or False.

import uuid
import re

# To generate a unique id on existing list
# for i in range(2):
#     unique_id = int(uuid.uuid4())
#     print(unique_id)

grocery_list: list[dict[str, float | int | bool | str]] = [

{
        "name": "Milk",
        "store": "Walmart",
        "cost": 6.47,
        "amount": 2,
        "priority": 1,
        "buy": True,
        "id": 279867738712164953486078660868091747138
},
    {
        "name": "Cheese",
        "store": "Walmart",
        "cost": 2.50,
        "amount": 1,
        "priority": 1,
        "buy": True,
        "id":115729385036103459303260851747783958910
    },
]


#Global variable
TAX = 0.08

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
    unique_id = int(uuid.uuid4())
    
    item = {
        "name": name, 
        "store": store, 
        "cost": cost, 
        "amount": amount, 
        "priority": priority, 
        "buy": buy,
        "id": unique_id
    }

    grocery_list.append(item)

def remove_item(id: int) -> None:
    
    """This is a function to remove items
        from the list as a string.

    Args:
        id (int): the assigned id for the item

    Returns:
        str: _return item as a string
    """
    
    index = get_index_from_id(id)
    grocery_list.pop(index)

def edit_item(
    name: str,
    store: str | None=None, 
    cost: float | None=None, 
    amount: int | None=None, 
    priority: int | None=None,
    buy: str | bool="skip", 
    id: int | None=None,
):
    """This is  function the allows the user to edit the items in a list.

    Args:
        name (str):The name of the item edit
        store (str | None)ed staore name. Defaults to none.
        cost (float | None):Updated cost. Defaults to None.
        amount (int | None): Updated amount. Defaults to None.
        priority (int | None): Updated priority. Defaults to None.
        buy (str | bool): Updated buy status. Defaults to "skip"
        id (str | None): Updated id.
    """
    
    index = get_index_from_id(id)
    old_item = grocery_list[index]
    
    if not store:
        store = old_item["store"]

    if not cost:
        cost = old_item["cost"]

    if not amount:
        amount = old_item["amount"]

    if not priority:
        priority = old_item["priority"]

    if buy == "skip":
        buy = old_item["buy"]

    if not id:
        id = old_item["id"]

    item = {
        "name": name, 
        "store": store, 
        "cost": cost, 
        "amount": amount, 
        "priority": priority, 
        "buy": buy,
        "id": id
        }
    
    if not name:
        name = old_item["name"]

    grocery_list[index] = item
   
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
                    f"name:{item['name']} -store:{item['store']} -"
                    f"cost: ${item['cost']} -amount: {item['amount']} -"
                    f"priority: {item['priority']}")
                
        total_cost = calculate_total_cost(buy_list, round_cost=True)
                
        print(f"The total cost is ${total_cost}")

def search_item_name(search_item):
    matching_items = []
    pattern = rf"^{search_item}"


    for item in grocery_list:
        if re.match(pattern, item["name"], re.IGNORECASE):
            matching_items.append(item)

    return matching_items


def get_index_from_id(id):
    index = 0
    for item in grocery_list:
        if item["id"] == id:
            return index
        else:
            index += 1

def get_index_from_name(name):
    index = 0
    
    """_The get_index_from_name(name) function 
will return the name of the item.

    Returns:
        _name_: _will return a string
    """

    for item in grocery_list:
        if item ["name"].lower() == name.lower(): 
            return index
        else:
            index += 1 

def list_items()-> str:
    """The list_items() function will list / print the items.

    Returns:
        str: -items as a string
    """
    for item in grocery_list:
        print(item)


def calculate_total_cost(grocery_list, round_cost=False):
    """_Parameters
    grocery_list (list[dict]): A list of dictionaries where each dictionary represents
    an item with keys 'amount' (int) and 'cost' (float).
    round_cost (bool): If True, rounds the total cost to the nearest integer. Default is False.
    tax (float): The tax rate to apply to the total cost. Default is the global TAX constant.

    Returns:
        _float: The total cost after applying tax and optional rounding.
    """
    total_cost = 0

    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    if round_cost:
        total_cost = round(total_cost)
        
    if TAX:
        tax_cost = total_cost * TAX
        total_cost += tax_cost

    return total_cost

    export_items()












