
"""
mk_core.py
This file is the core file that provides the functions for the app.
It includes the ability to add, remove, edit, search and export the list.

Functions are:
-add_items(): Add items to the list.
-remove_items(): Removes items from the list.
-edit_items(): Edits any item within the list. Any value can be edited.
-export_items(): Able to export the list.
-search_items(): Able to search for items if there are duplicates using id number.

Author: Mike Kwiatkowsky
Version:2.0.0
"""
# The grocery_list is a list of items showing the keywords and values of each.
# Also this shows the type of item within the list ex: "name" is a string,
# cost is a float, priority is an integer and buy is a boolean.-True or False.

import logging
import os
import re
import uuid

import constants
import utils
import log_config

TAX = 0.08

def get_grocery_list():
    os.makedirs(constants.EXPORT_PATH, exist_ok=True)
    file_path = os.path.join(
        constants.EXPORT_PATH, f"{constants.GROCERY_LIST}.json")

    if os.path.exists(file_path):
        grocery_list = utils.load_data(file_path)

    else:
        print("No json path found, creating JSON path")
        grocery_list = []
        utils.save_data(file_path, grocery_list)

    return grocery_list

def get_index_from_id(id):
    index = 0
    grocery_list = get_grocery_list()

    for item in grocery_list:
        if item["id"] == id:
            return index
        else:
            index += 1

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


def get_index_from_name(name):
   
    """_The get_index_from_name(name) function 
will return the name of the item.

    Returns:
        _name_: _will return a string
    """
    index = 0
    grocery_list = get_grocery_list()

    for item in grocery_list:
        if item ["name"] == name:
            return index
        else:
            index += 1 

def add_item(name, store, cost, amount, priority, buy):
    """Add a new item to the list.

    Args:
        name (str): a string
        store (str): a string
        cost (float): a float
        amount (int): an integer
        priority (int): an integer
        buy (bool): a boolean
        id (int): Automatically generated
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

    grocery_list = get_grocery_list()
    grocery_list.append(item)

    file_path = os.path.join(constants.EXPORT_PATH, f'{constants.GROCERY_LIST}.json')

    utils.save_data(file_path, grocery_list)
    
def remove_item(id: int) -> None:
    
    """This is a function to remove items
        from the list as a string.

    Args:
        id (int): the assigned id for the item

    Returns:
        str: _return item as a string
    """
    
    index = get_index_from_id(id)
    grocery_list = get_grocery_list()
    grocery_list.pop(index)

    file_path = os.path.join(constants.EXPORT_PATH, f'{constants.GROCERY_LIST}.json')
    utils.save_data(file_path, grocery_list)
    
    
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
    old_item = get_grocery_list()

    if not name:
        name = old_item["name"]
    
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
    
    grocery_list = get_grocery_list()
    grocery_list[index] = item

    file_path = os.path.join(constants.EXPORT_PATH, f'{constants.GROCERY_LIST}.json')
    utils.save_data(file_path, grocery_list)
    logging.info(
        f"Added: {name} {store} {cost} {amount} {priority} {buy} {id}"
    )

def list_items(grocery_list)-> str:
    """The list_items() function will list / print the items.

    Returns:
        str: -items as a string
    """
    for match_num, item in enumerate(grocery_list, start=1):
        match_string = (
            f"{match_num}. |"
            f"Name: {item["name"]}, |"
            f"Store: {item["store"]}, |"
            f"Cost: {item["cost"]}, |"
            f"Amount: {item["amount"]}, |"
            f"Priority: {item["priority"]},| "
            f"Buy: {item["buy"]}"
        )
        
        print(match_string)  
        
          

def export_items(grocery_list):
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
                    f"name:{item['name']} |store:{item['store']} |"
                    f"cost: ${item['cost']} |amount: {item['amount']} |"
                    f"priority: {item['priority']}")
                
            total_cost = calculate_total_cost(buy_list, round_cost=True)
    print(f"The total cost is ${total_cost}")

    

def search_item_name(search_item):
    matching_items = []
    pattern = rf"^{search_item}"

    grocery_list = get_grocery_list()
    
    for item in grocery_list:
        if re.match(pattern, item["name"], re.IGNORECASE):
            matching_items.append(item)

    return matching_items


    export_items()












