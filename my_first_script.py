# print("Hello, World!")

# Day 2 Exercise
# =======================================================
# Exercise 1
# bread = 3.25
# steak = 8.40
# milk = 2.51
# total_cost = bread + steak + milk

# print(f"Your total is: ${total_cost}")
# # =======================================================
# # Exercise 2

# # Obtain store name from user
# store_name = input("What's the name of your favorite grocery store?")

# # Welcome user to their favorite store
# print(f"Welcome to {store_name}!")
# # ========================================================
# # Exercise 3
# milk = int("3")
# bread = 2.5
# total = str(milk + bread)
# print("The total cost is: $" + total)
# # ========================================================


# #Day 3 Exercises

# apples_tuple = ("apples", 0.50, 5)
# pears_tuple = ("pears", 1050, 2)
# bananas_tuple = ("bananas", 1.99, 5)


# # Day 3: Lists and Tuples
# # Lists
# my_list=[1, "apple", 3.5]
# print(my_list)

# # Index
# my_list[0]
# print(my_list)

# # Slice
# my_list[1:3]
# print(my_list)

# # Add
# my_list.append("banana")
# print(my_list)

# # Remove
# my_list.remove("apple")
# print(my_list)

# # Sort
# my_int_list=[5, 9, 3, 11]
# my_int_list.sort()
# print(my_list)

# # Extend
# list_a=[1, "apple", 3.5]
# list_b=["banana", "tomato"]
# list_a.extend(list_b)
# print(my_list)

# # Insert at specific index
# my_list.insert(1, "banana")
# print(my_list)

# # Tuples
# my_tuple = (10, 20, "orange")
# print(my_tuple)

# # Index
# print(my_tuple[0])

# # Slice
# print(my_tuple[0:2])

# # Length
# print(len(my_tuple))

# # Concatenate
# print(my_tuple + (30, 40))
# # ========================================

# List Practice Exercises

# 1.
# favorite_movies = ["Star Wars", "The Godfather", "Casino", "The Matrix", "Love Actually"]
# print(favorite_movies)
# favorite_movies.append("The Hangover")
# print(favorite_movies)
# favorite_movies.remove("The Godfather")
# print(favorite_movies)

# # 2.
# numbers =[10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[3:5])

# # 3.
# colors = ["red", "blue", "green"]
# print(colors)
# colors.insert(1, "yellow")
# colors.append("purple")
# print(colors)

# # Tuple Practice Exercises

# # 1.
# dimensions = (10, 5, 20)
# print(dimensions[1])

# # 2.
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# print(numbers[2:6])

# # 3.
# fruits = ("apple", "banana")
# vegitables = ("carrot", "lettuce")
# groceries = fruits + vegitables
# print(groceries)

# ======================================================

# Dictionaries

# Syntax
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# # Access values
# print(my_dict['name'])

# # Adding or updating values
# a_dict = {'name': 'John', 'age': 25}
# a_dict['city'] = 'New York'
# a_dict['age'] = 26
# print(a_dict)

# # Removing values
# b_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# b_dict.pop('age')
# print(b_dict)

# ========================================================
# Dictionary Practice Exercerises
# 1
# book = {'tite': '1984', 'author': 'George Orwell', 'year': 1949}
# print(book['author'])

# #2
# profile = {}
# profile.update({'name': 'Alice', 'age': 30, 'city': 'Paris'})
# print(profile)
# profile['city'] = 'London'
# print(profile)

# #3
# student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
# print(student)
# student.pop('subject')
# print(student)
# print(student.keys())
# print(student.values())
# ============================================================

# Sets
# Syntax
# my_set = {'apple', 'banana', 'cherry'}
# print(my_set)

# # Adding
# my_set.add('orange')
# print(my_set)

# # Removing
# my_set.remove('orange')
# print(my_set)

# # Discard
# my_set.discard('banana')
# print(my_set)

# # Set Operations
# # Union
# set1 = {'apple', 'banana'}
# set2 = {'banana', 'orange'}
# print(set1.union(set2))

# #  Intersection
# print(set1.intersection(set2))

# # Diffence
# set1.add('cherry')
# print(set1.difference(set2))

# =========================================
# Set Practice Exercise

# 1
# fruits = {'apple', 'banana', 'cherry'}
# print(fruits)
# fruits.add('orange')
# print(fruits)
# fruits.discard('banana')
# print(fruits)

# 2
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a)
# print(set_b)
# print(set_a.union(set_b))
# print(set_a.intersection(set_b))

# # 3
# set_x = {'cat', 'dog', 'fish'}
# set_y = {'dog', 'bird'}
# print(set_x)
# # print(set_y)
# # print(set_x.difference(set_y))

# # ============================================
# # Day 3 Required Assignments

# # Exercise 1
# # 1
# bananas_tuple = ('bananas', 0.73, 8)
# cherries_tuple = ('cherries', 1.16, 4)
# apples_tuple = ('apples', 1.27, 5)
# # 2
# grocery_list = []
# print(grocery_list)
# grocery_list = [bananas_tuple] + [cherries_tuple] + [apples_tuple]
# print(grocery_list)
# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[-1])

# #3
# bananas_total_cost = grocery_list[0][1] * grocery_list[0][2]
# cherries_total_cost = grocery_list[1][1] * grocery_list[1][2]
# apples_total_cost = grocery_list[2][1] * grocery_list[2][2]
# print(f'Total cost of {grocery_list[0][0]}: ${bananas_total_cost}')
# print(f'Total cost of {grocery_list[1][0]}: ${cherries_total_cost}')
# print(f'Total cost of {grocery_list[2][0]}: ${apples_total_cost}')

# # Exercise 2
# # 1
# bananas_dict = {'name': 'bananas', 'price': 0.73, 'quantity': 8, 'total_cost': 5.84}
# cherries_dict = {'name': 'cherries', 'price': 1.16, 'quantity': 4, 'total_cost': 4.64}
# apples_dict = {'name': 'apples', 'price': 1.27, 'quantity': 5, 'total_cost': 6.35}
# print(f'Total cost of {bananas_dict['name']}: ${bananas_dict['total_cost']}')
# print(f'Total cost of {cherries_dict['name']}: ${cherries_dict['total_cost']}')
# print(f'Total cost of {apples_dict['name']}: ${round(apples_dict['total_cost'],2)}')

# # Exercise 3
# # 1
# num_list = [16, 47, 1, 3, 5, 9, 15, 2]
# print(num_list)
# print(num_list[1:])
# print(num_list[:3])
# print(num_list[-3])

# # 2
# num_list.sort()
# print(num_list)

# #3
# print(len(num_list))

# # Exercise 4
# # 1
# dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
# print(dairy_products)
# desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}
# print(desserts)

# # 2
# dairy_products.add('ice creame')
# print(dairy_products)
# desserts.add('ice creame')
# print(desserts)

# # 3
# dairy_products.remove('cream')
# print(dairy_products)
# desserts.discard('jello')
# print(desserts)

# # 4
# print(dairy_products.intersection(desserts))

# =====================================================
# Day 4 Conditional DStatements
# IF ELIF, and ELSE


# if first_condition:
#     # Code to execute if first condition is true
# elif second_condition:
#     # Code to execute if first_condition is false but
#       second_condition is true
# elif third_condition:
#     # Code to execute if first_condition and second_condition
#       are false but third_condition is true
# else:
#     # Code to execute if none of the conditions are true

# Key Operations
# IF statement runs code if condition is true

# price = 20
# if price < 30:
#     print("This is affordable.")

# ELIF Statement: Adds an additional condition if the first if is false.

# price = 35
# if price < 30:
#     # This will be skipped because price is more than 30
#     print("This is affordable.")
# elif price < 40:
#     # It will run this code here instead
#     print("This is a bit expensive.")

# #ELSE Statement: Runs if none of the if or elif conditions are met.
# price = 50
# if price < 30:
#     # This will be skipped because price is more than 30
#     print("This is affordable.")
# elif price < 40:
#     # This will also be skipped because price is more than 40
#     print("This is a bit expensive.")
# else:
#     # It will run this code here instead
#     print("This is too expensive.")


# Nested Conditionals
# a conditional placed inside another conditional, enabling complex, layered decision-making based on multiple criteria.
# every nested conditional should be indented to separate it from other conditionals.
# if first_conditional:
#     if nested_conditional: # Indented from the first conditional
#         print(“I satisfy the nested conditional”)

# Full example:
# weather = "sunny"
# temperature = 75


# conditional 1: Check if the weather is sunny or not
# if weather == "sunny":
#     # conditional 2: if sunny, check if temperature is above 70
#     if temperature > 70:
#         print("Wear sunglasses and a t-shirt.")
#     else: # matching else statement for conditional 2
#         print("Wear sunglasses and a light jacket.")
# else: # matching else statement for conditional 1
#     print("Bring an umbrella.")


# =====================================================
# Practice Exercises

# 1.
# number = int(input("Give me a number: "))

# if number % 2 == 0:
#     print("Even")
# else:clear

#     print("Odd")


# 2 IF-ELIF-ELSE-CHAIN
# temp = int(input("Enter the temperature in Clecius of Farenheit:c "))
# if temp < 15:
#     print("Cold")
# elif temp  <25 :
#     print("Warm")
# else:
#     print("Hot")


# 3 Nested Conditionals

# if first_conditional:
#     if nested_conditional: # Indented from the first conditional
#         print(“I satisfy the nested conditional”)

# Full example:
# weather = "sunny"
# temperature = 75


# conditional 1: Check if the weather is sunny or not
# if weather == "sunny":
#     # conditional 2: if sunny, check if temperature is above 70
#     if temperature > 70:
#         print("Wear sunglasses and a t-shirt.")
#     else: # matching else statement for conditional 2
#         print("Wear sunglasses and a light jacket.")
# else: # matching else statement for conditional 1
#     print("Bring an umbrella.")

# Practice Exercises
#=================================================
#! Basic IF-ELSE

# number = int(input("Give me a number"))


# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# IF-ELIF-ELSE-CHAIN
# Cold Warm Hot

# temp = int(input("Enter a temp in Celsius or Farenheit:"))

# if temp < 15:
#     print("Cold")
# elif temp <25:
#     print("Warm")
# else:
#     print("Hot")

# 3 Nested Conditionals

# age = int(input("Enter your age: "))
# citizenship = input("Are you a citizen?(yes/no): ").lower()
# if age > 18:
#     if citizenship == "Yes":
#         print("You are eligble to vote.")
#     else:
#         citizenship == "No"
#         print("Not eligible.")
# else:
#     print("Not eligible: Must be 18 or older.")

# LOOPS
#===================================================

# FOR and WHILE
# Definition: Loops allow repetitive execution of code blocks.
#  Use for to iterate over sequences and while to repeat until a condition is false.

# Syntax: 
# 	loop:  for or while
# colon “ : ”  
# Indent:  press ‘tab’ OR add 4 blank spaces (preferred) before
#  the code that gets executed after each loop statement . (NOTE: vscode automatically adds indentation for you.)
# for loop:
# for item in sequence: 
#     # Code to execute for each item

# while loop:
# while condition: 
#     # Code to execute as long as condition is true


# Key Operations:
# For Loop: Used for iterating over lists, strings, or other iterable sequences.
# items = ["apple", "banana", "cherry"]
# for item in items:
#     print(item)


# While Loop: Used when you don’t know the number of repetitions in advance.
# count = 0 
# while count < 5:
#     print("Counting:", count)
#     count += 1



# Nested Loops
# a loop placed inside another loop, allowing complex, 
# repeated actions within each iteration of the outer loop.
# each nested loop should be indented to clearly distinguish it from the outer loop

# for outer_item in outer_sequence:
#     for inner_item in inner_sequence:  # Indented to show it's nested
#         print("This is a nested loop example.")


# Full example:
# shape_list = ["circle", "square", "triangle"]
# color_list = ["red", "yellow", "green"]

# # Outer loop: Iterate over each shape
# for shape in shape_list:
#     # Inner loop: Iterate over each color
#     for color in colors:
#         print(f"{shape} is {color}")

# #RESULT:
# circle is red
# circle is yellow
# circle is green
# square is red
# square is yellow
# square is green
# triangle is red
# triangle is yellow
# triangle is green


# Practice Exercises
#1 Basic for Loop: Create a for loop that prints each item in a list of groceries.
# shop_list = [
#     {
#         "name": "milk", "amount": 2,  "cost": 2.5, "store": "Wal-Mart",
#     }, 
#     {
#         "name": "bread", "amount": 1, "cost": 1.5, "store": "Acme",

#     },
#     {
#         "name": "eggs", "amount":12,  "cost": 3, "store": "Hyeks",
#     }
# ]
# for item in shop_list:
#     print(item)

# #2 While Loop with User Input: Write a program that lets the user add items to a grocery list until they type "done."
# while True:
#     command = input("Type a command add or done: ")
#     if command == "done":
#         break

#     name = input("Enter item name: ")
#     amount = int(input("Enter amount: "))
#     cost = float(input("Enter cost: "))
#     store = input("Enter store: ")

#     new_item_dict = {"name" : name, "amount": amount, "cost": cost, "store": store}
#     shop_list.append(new_item_dict)

# print(f"{name} was added to the shopping list")
# print(shop_list)



# #3 Loop through a Dictionary: Using a grocery list with item details, loop through and print each item’s name and total cost.
# for item in shop_list:
#    print(f"{item['name']} - {item['amount']} units- ${item['cost']} - from {item['store']}")

# #====================================================

#Loop Control


# BREAK, CONTINUE, and PASS

# Definition: Loop control statements allow you to manage loop flow

# BREAK: Stops the loop when a condition is met. 
# for item in ["apple", "banana", "cherry", “mango”]:
#     if item == "banana":
#         break
# print(“{item} is yellow.”)

# # Output: 
# banana is yellow.


# Code Breakdown:
# First iteration: apple. This is not "banana" so the loop will continue to proceed to the next item.
# Second iteration: banana. This satisfies the condition and will stop the loop. ‘banana’ will be assigned to the variable ‘item’.
# break: The loop ends at banana and ultimately skips “cherry” and “mango”

# CONTINUE: Skips the current loop iteration.
# yellow_fruits = ["banana", "mango"]
# red_fruits = []

# for item in ["apple", "banana", "cherry", "mango"]:
#     if item in yellow_fruits:
#         continue
#     red_fruits.append(item)

# # Output:
# ['apple', 'cherry']

# TIP: The operator in checks for membership. You can use it to see if a string contains a specific substring or if the current item belongs to a list/set/dictionary. 

# Code Breakdown:
# First iteration: apple.  ‘apple’ does not satisfy the condition because it is not included in the ‘yellow_fruits’ list. So the next line of code executes and apple is added to the ‘red_fruits’ list.
# Second iteration: banana.  ‘banana’ is in the ‘yellow_fruits’ list so our loop will just continue and the next line of code does not get executed. 
# Third iteration: cherry. Same as ‘apple’, it doesn't belong to the ’yellow_fruits’ list so we execute the next code and add it to the ’red_fruits’ list
# Fourth iteration: mango. Same as ’banana’, it is part of the ‘yellow_fruits’ list so we skip this. 


# PASS: Acts as a placeholder allowing the loop to continue without action
# for item in ["apple", "banana", "cherry", “mango”]:
#     if item == "banana":
#         pass  # Does nothing
#     print(item)

# # Output
# apple
# banana
# cherry
# mango

# Practice Exercises

#1. Using Break: Write a loop that stops when a specific item is found in a list.
# for item in ["apple", "grapes", "bananas", "oranges"]:
#     if item == "oranges":
#         break
# print(f"{item} was found.")


#2. Using Continue: Create a loop that skips specific items (e.g., non-fruit items) in a grocery list.

# fruits = ["apple", "cherry"]
# new_fruits = []

# for item in ["apple", "banana", "cherry", "mango"]:
#     if item in fruits:
#         continue
#     new_fruits.append(item)
# print(new_fruits)


#3. Using Pass: Write a loop that uses pass for an item to act as a placeholder for future code.

# for item in ["apple", "banana", "cherry", "mango"]:
#     if item  == "apple":
#         pass
#     print(item)
# #================================

# #Traceback
# Day 4: Error Handling and Debugging
# TRY and EXCEPT
# Definition: Error handling allows you to manage program errors gracefully using try and except. Debugging includes reading error messages (tracebacks) and solving logic errors (like infinite loops)
# Syntax: 
# try:
#     # Code to try
# except ErrorType:
#     # Code to execute if error occurs


# Key Concepts:
# Try-Except: Catches specified errors, allowing the program to handle them.
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# TIP: You can handle multiple error types in a single except block by listing them in parentheses/ tuple of errors. For example:
# try:
#     # some code that may cause an error
# except (TypeError, ValueError) as e:
#     print(f"An error occurred: {e}")


# Here, except (TypeError, ValueError) as e will catch either a TypeError or ValueError and store the error message in a variable,  e, making it easy to print or log the actual error. 

# !! You don’t have to worry about error types for now but if you’re curious, you can view built in exceptions here:  https://docs.python.org/3/library/exceptions.html !!
# Traceback: Identifies the error type and the line number in the code where the error occurred.

# TIP: To troubleshoot errors, start from the bottom of the traceback and work your way up. In the example below, you would begin by inspecting line 2, as it’s where the error occurred. If the issue isn’t clear there, then move up to line 6 to check the previous calls that led to the error.

# Traceback (most recent call last):
#   File "example.py", line 6, in <module>
#     result = divide_numbers(10, 0)
#   File "example.py", line 2, in divide_numbers
#     return a / b
# ZeroDivisionError: division by zero


# Avoiding Infinite Loops in while: Ensure the loop’s condition will eventually become false.
# count = 0
# while count < 5:
#     print(count)
#     count += 1  # Ensures the loop will end


# Practice Exercises
# 1. Using Try-Except: Create a script that prompts the user for a number. 
# If they enter non-numeric input, handle the error gracefully.
# A) Use input() to get input from the user.
# B) Use try to attempt converting the input to an integer or float.
# C) Inside the try block, print the number if conversion is successful.
# D) Use except to catch ValueError if the input is non-numeric.
#  E) Expected output:
# # If input is a number
# Enter a number: 42 
# You entered the number: 42.0
# # If input is NOT a number:
# Enter a number: abc
# Error: Please enter a valid number.

# number = input("Enter a number: ")
# try:
#     float(number)   
#     print(f"You entered the niumber: {number}")
# except ValueError:
#     print("Erro occured: the input is not a number")



#Reading Tracebacks: Run the code below and find the issue in the code by reading the traceback you get
# a = 10
# b = 5

# # # Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
# double_b = b * 2

# # # Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
# total = a + double_b

# print("The total is:", total)

#================================================

#Day 4 Assignments
# # Exercise 1
# grocery_item = []
# grocery_item.append(input("Enter the name of the item to add to your grocery list: "))
# food_items = ["apple", "bread", "milk"]
# non_food_items = ["soap", "detergent", "paper towels"]

# for item in grocery_item:
#     if item in food_items:
#         print(f"{item} is on the food items list.")
#     elif item in non_food_items:
#         print(f"{item} is on the non-food items list.")
#     else:
#         print(f"{item} is not on any know list.")


# # Exercise 2
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = 0

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1

# print(shopping_list)

# # Exercise 3
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = 0

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     for name in shopping_list:
#         print(name)
#     print("----------")
# print(shopping_list)

# # Exercise 4
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = a

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     for name in shopping_list:
#         print(name)
#     print("----------")
#     if "burger buns" in shopping_list and "fries" in shopping_list and "burger patties" in shopping_list:
#         print(f"We can make burgers and fries for {total_cost}")
#         break
# print(shopping_list)

# # Exercise 5
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = a

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     try:
#         int(index)
#     except ValueError:
#         print("Error: the index must be an integer")
#     for name in shopping_list:
#         print(name)
#     print("----------")
#     if "burger buns" in shopping_list and "fries" in shopping_list and "burger patties" in shopping_list:
#         print(f"We can make burgers and fries for {total_cost}")
#         break
# print(shopping_list)

# # Exercise 6
items_list = [
    {"name": "Ice Cream", "cost":5.25, "amount": 1},
    {"name": "Hot Fudge", "cost":0.99, "amount": 1},
    {"name": "Whip Cream Topping", "cost": 0.25, "amount": 1},
]

shopping_list = []
budget = 30.0
total_cost = 0.0
index = 0

while total_cost <= budget:
    item = items_list[index]
    item_total_cost = item["cost"] * item["amount"]
    if total_cost + item_total_cost > budget:
        break
    shopping_list.append(item["name"])
    total_cost += item_total_cost
    index += 1
    try:
        int(index)
    except ValueError:
        print("Error: the index must be an integer")
    for name in shopping_list:
        print(name)
    print("----------")
    if "Ice Cream" in shopping_list and "Hot Fudge" in shopping_list and "Whip Cream Topping" in shopping_list:
        print(f"We can make a hot fudge sunday for ${total_cost}")
        break
print(shopping_list)




