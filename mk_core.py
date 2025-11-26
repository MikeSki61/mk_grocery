#Default groceey list
grocery_list = [
    {"name": "milk", "store": "Wal-Mart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True},
]

#Global variable
tax = .08

# Function to add items to your grocery list
def add_item(name, store, cost, amount, priority, buy):
    # Defined dictionary item to add to list
    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}
    # Defined dictionary item to add to list
    grocery_list.append(item)

def remove_item(name):
    index = get_index_from_name(name)

    grocery_list.pop(index)

def edit_item(name, store= None, cost= None, amount= None, priority= None, buy=None):
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

    item = {"name": name, "store": store, "cost": cost, "amount": amount, "priority": priority, "buy": buy}

    grocery_list[index] = item
    
def export_items():
    buy_list = []

    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)

    if buy_list:
        for item in buy_list:
            print(f"name:{item['name']} -store:{item['store']} - cost: ${item['cost']} - amount: {item['amount']} -priority: {item['priority']}")
            
        total_cost = calculate_total_cost(buy_list, round_cost = True)
        
def get_index_from_name(name):
    index = 0

    for item in grocery_list:
        if item ["name"] == name:
            return index
        else:
            index += 1

def list_items():
    for item in grocery_list:
        print(item)

def calculate_total_cost(grocery_list, round_cost = False, tax= 0.08):
    total_cost = 0
    
    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    if round_cost:
        total_cost = round(total_cost)
        
    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost

    return total_cost

export_items()












