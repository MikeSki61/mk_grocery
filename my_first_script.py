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
# items_list = [
#     {"name": "Ice Cream", "cost":5.25, "amount": 1},
#     {"name": "Hot Fudge", "cost":0.99, "amount": 1},
#     {"name": "Whip Cream Topping", "cost": 0.25, "amount": 1},
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
#     try:
#         int(index)
#     except ValueError:
#         print("Error: the index must be an integer")
#     for name in shopping_list:
#         print(name)
#     print("----------")
#     if "Ice Cream" in shopping_list and "Hot Fudge" in shopping_list and "Whip Cream Topping" in shopping_list:
#         print(f"We can make a hot fudge sunday for ${total_cost}")
#         break
# print(shopping_list)


#====================================================
#Day 5 Functions and Modules
# def my_first_function():
#     print("This is a function")

# my_first_function()

# What is a Function?
# Definition: A function is a block of code that performs a specific task. 
# You define it once, then you can use it (or “call” it) whenever you need that task done.
# SYNTAX
# def :every function begins with this keyword
# function name :what you want to call the function ‘my_function_to_add’
# parenthesis () :this is where parameters live
# parameters  :variables that can be used as inputs of the function
# colon : marks the end of your function definition.  
# Indentation :the actual code block running the logic should be indented 

# Example:
# def print_something():
#     print("Look! I’m printing something!")

# CALLING A FUNCTION
# Call (or "run") the function by typing its name followed by parentheses.

# Example:
# print_something()
# Look, I'm printing something!  # Result

# 3. Creating Your Own Functions
# Think about tasks you often repeat, like displaying messages or simple calculations.
# Functions make your code more organized and reusable.

# 4. Function Naming Tips
# Use descriptive names (like show_message or calculate_total).
# Use lowercase letters and underscores between words for readability (snake_case).

# Practice Exercises
# Exercise 1: Displaying a Message
# Define a function that prints a welcome message.
# Call the function to see the message.

# def greeting():
#     print("Hello, welcome to this course.")
# greeting()

# Exercise 2: Print Your Favorite Food
# Write a function named favorite_food that prints your favorite food.
# Call the function to display the food.

# def fav_food():
#     print("My favorite food is Italian")
# fav_food()

# Exercise 3: show sum of numbers
# Create a function named show_sum that adds 5 and 10, and then prints the result.
# Call show_sum to see the result in action.

# def show_sum():
#     print(5 + 10)
# show_sum()


# Day 5: Parameters and Return Values
# What Are Parameters?
# Definition: Parameters are like placeholders in a function 
# definition that let us pass data into the function. 
# They help make functions more flexible and useful by allowing them 
# to work with different inputs each time we call them.

# Mandatory vs Optional Parameters
# Mandatory parameters  are variables that the user needs to provide in order for the
#  function to run. Optional Parameters are variables that are not required so the function will 
# still run even if this is not provided during a function call and stores a default value for that parameter. 

# Example: Write a function that prints the items in a grocery list. 

# Step 1: Define the function.  We will use ‘grocery_list’ as the placeholder/parameter  
# that will represent all the potential grocery lists we will use as input
# def print_grocery_list_items(grocery_list):


# Step 2: Code Block. What code needs to run to accomplish the task? 
# print(grocery_list)


# Putting them together:
# def print_grocery_list_items(grocery_list):
#     print(grocery_list) # Make sure code block is indented


# In this example, grocery_list is a mandatory/required parameter because the function 
# cannot run without it. 

# Step 3: Call and Test the function. Use different grocery lists to see if it prints them based on which list you use as input
# # Our Function:
# def print_grocery_list_items(grocery_list):
#     print(grocery_list)

# # Test Lists:
# fruits_grocery_list = ['apple', 'banana', 'grapes']
# veggie_list = ['kale', 'eggplant', 'spinach', 'broccoli']
# misc_items = ['shampoo', 'dishsoap', 'sponges']

# # Test 1:
# print_grocery_list_items(fruits_grocery_list)
# ['apple', 'banana', 'grapes']  # RESULT

# # Test 2:
# print_grocery_list_items(veggie_list)
# ['kale', 'eggplant', 'spinach', 'broccoli']  # RESULT

# # Test 3:
# print_grocery_list_items(misc_items)
# # ['shampoo', 'dishsoap', 'sponges']  # RESULT

 
# # Step 4: Improve the function if possible.  To make the output look cleaner, we can be more explicit with what we are printing and instead of printing the list as-is, we can use a for loop to print each item one at a time.
# def print_grocery_list_items(grocery_list):
#     print("We need to buy the following: ") # Be more explicit 
#     for item in grocery_list:
#         print(item)  # print each item one at a time

# # # Call the function using fruits_grocery_list
# print_grocery_list_items(fruits_grocery_list)

# # RESULT:
# We need to buy the following:
# apple
# banana
# grapes

# Step 5: Extend the functionality using optional parameters. We will use ‘nice_to_have_list’ as an 
# optional parameter to include items that we want but don’t necessarily need to buy. 

# Note: A parameter becomes optional when you give it a default value. 
# Remember to ALWAYS put optional parameters after the required parameters. 

# def print_grocery_list_items(grocery_list, nice_to_have_list=None):


#  In this case, the default value of nice_to_have_list is None, meaning we don’t have 
# a ‘nice to have’ list. This is optional because the function can still run 
# even if this input is not provided. It mainly says that the function will 
# perform additional/different tasks if the value is different from the default.

# Step 6: Additional task for optional parameter. What will the function do if the 
# user provides a value for nice_to_have_list?
# New Task:  if we provide a nice to have list, then we want to print that “If possible, 
# it would be nice to buy the following as well:” 

# if nice_to_have_list != None:  # != means 'not equal to' 
#     print("If possible, it would be nice to buy the following as well:")
#     for item in nice_to_have_list:
#         print(item)


# We can further improve this block by using 
# if nice_to_have_list:

# This checks for empty values. So instead of just checking if this variable is NOT None, we are also making sure that  nice_to_have_list is NOT 0, [ ] (an empty list), { } (an empty dictionary/set),   ‘ ’ ( a blank string), or False. 

# Putting it all together we have:


def print_grocery_list_items(grocery_list, nice_to_have_list=None):
    print("We need to buy the following: ")
    for item in grocery_list:
        print(item) 

    if nice_to_have_list:
        # ‘\n’ means new line. So this will add a blank line
        print("\nIf possible, it would be nice to buy the following as well:")
        for item in nice_to_have_list:
            print(item)



# Step 7: Test the optional parameter. Create a test list and try calling the function with and without the optional parameter. 
# # test list
# desserts_list = ['tiramisu', 'ice cream', 'candy bar']
# fruits_grocery_list = ['apple', 'banana', 'grapes']

# # Call the function WITHOUT the optional parameter
# print_grocery_list_items(fruits_grocery_list)

# # RESULT:
# We need to buy the following:
# apple
# banana
# grapes

# # Call the function WITH the optional parameter
# print_grocery_list_items(fruits_grocery_list, nice_to_have_list=desserts_list)

# # RESULT:
# We need to buy the following:
# apple
# banana
# grapes

# If possible, it would be nice to buy the following as well:
# tiramisu
# ice cream
# candy bar

# More Examples of a Function with Parameters
# Let’s create a function that checks if a certain grocery item is available in stock. The function will take two parameters: item_name and stock_status.
# def check_availability(item_name, stock_status):
#     if stock_status:
#         print(f"{item_name} is available.")
#     else:
#         print(f"{item_name} is out of stock.")


# Here, item_name and stock_status are parameters. Each time we call check_availability(), we can pass in different items and stock statuses:
# check_availability("Bananas", True)   
# # Output: Bananas is available.

# check_availability("Milk", False)     
# # Output: Milk is out of stock.



# Multiple Parameters
# You can add more parameters as needed but make sure that you follow the same sequence of parameters when calling the function. For instance, let’s add a store_name parameter to specify where the item is available:
# def check_availability_in_store(item_name, stock_status, store_name):
#     if stock_status:
#         print(f"{item_name} is available at {store_name}")
#     else:
#         print(f"{item_name} is out of stock at {store_name}")


# Now, we can specify the store name each time we call check_availability_in_store():
#                         # item_name  stock_status  store_name
# check_availability_in_store("Apples", True, "SuperMart")    
# # Output: Apples is available at SuperMart.
#                         # item_name  stock_status  store_name
# check_availability_in_store("Eggs", False, "Fresh Foods")   
# # Output: Eggs is out of stock at Fresh Foods.

 
# What Is A Return Value?
# Definition: A return value is the result a function gives back after it completes a task. Instead of just printing something, the function returns data so we can store it a variable and use it elsewhere in the code

# Example:
# Write a function that returns a message about the freshness of produce:
# def check_freshness(item_name, days_since_purchase):
#     if days_since_purchase < 3:
#         return f"{item_name} is fresh."
#     else:
#         return f"{item_name} might be past its prime."


# Here, check_freshness() returns a message based on how many days have passed. We can store this result in a variable or use it directly:
# message = check_freshness("Lettuce", 3)
# print(message)                    
# # Output: Lettuce is fresh.

# print(check_freshness("Tomatoes", 7))  
# # Output: Tomatoes might be past its prime.


# Why Use Return Values?
# Return values allow us to get information back from a function and use it elsewhere in the code, making our functions more versatile.
# Practice Exercises
# Exercise 1: Grocery Item Search
# Create a function find_item that takes two parameters, item_name and is_available, and prints whether or not the item is available.
# def find_item(item_name, is_available):
#     if is_available:
#         return f"{item_name} is available."
#     else:
#         return f"{item_name} is not available."

# message = find_item("Orange Juice", True)
# print(message)
# message = find_item("Bread", False)
# print(message)

# Example Output:
# find_item("Orange Juice", True)   
# # Expected output: Orange Juice is available.

# find_item("Bread", False)         
# # Expected output: Bread is not available.


# Exercise 2: Favorite Snack
# Write a function favorite_snack that takes two parameters, snack_name and quantity_left, and returns a message based on how much of the snack is left.

# # 2
# def favorite_snack(snack_name, quantity_left):
#     if quantity_left:
#         return f"You have some {snack_name} left to enjoy!"
#     else:
#         return f"You are out of {snack_name}."

# print(favorite_snack("Chips", 3))
# print(favorite_snack("Cookies", 0))
# Example Output:
# print(favorite_snack("Chips", 3))  
# # Expected output: You have some Chips left to enjoy!
# print(favorite_snack("Cookies", 0)) 
#  # Expected output: You're out of Cookies!


# Exercise 3:  Store Item Location
# Create a function item_location that takes two parameters, item_name and store_section, 
# and returns a message about where to find the item in the store.
# def item_location(item_name, store_section):
#     return f"You can find {item_name} in the {store_section}."

# print(item_location("Milke", "Dairy Aisle"))
# print(item_location("Apples", "Produce Section"))

# Example Output:
# print(item_location("Milk", "Dairy Aisle"))      
# # Expected output: Find Milk in the Dairy Aisle.

# print(item_location("Apples", "Produce Section")) 
# # Expected output: Find Apples in the Produce Section.


# Day 5: Scope and Lifetime of Variables
# Variable Scope and Lifetime in Python help us control where and how long 
# variables are accessible in our code. Understanding these concepts can 
# prevent errors and improve code organization.

# SCOPE OF VARIABLES
# Definition: Scope defines where in your program you can use a variable. 
# It determines where a variable can be accessed. There are two main types of scope:
# Global Scope: Variables defined outside of any function or block. Accessible throughout the entire program.
# Example:
# message = "I love chocolate!"
# def chocolate():
#     print(message)

# # test inside a function
# chocolate()
# I love chocolate!  # output

# # test outside a function
# print(message)
# I love chocolate!  # output

# In this case, ‘message’ is defined outside any function, so it has global scope and is accessible anywhere in the program.
# TIP: Global constants, which do not change, are usually written in uppercase (e.g., PI = 3.14159).
# Local Scope: Variables defined within a function or block. Accessible only within that specific function or block.
# Example:
# def chocolate():
#     message = "I love chocolate!"
#     print(message)

# # test inside a function
# chocolate()
# I love chocolate!  # output

# # test outside a function
# print(message)  
# Error: NameError - 'message' is not defined  # Errors out


# In this example, message is defined inside the chocolate() function, making it 
# local to chocolate. It is inaccessible outside this function.




# LIFETIME OF VARIABLES
# Definition: Lifetime refers to how long a variable exists in memory.
# Global Variables exist throughout the entire runtime of the program.
# Local Variables only exist during the execution of the function in which 
# they’re defined. Once the function completes, these variables are discarded.
# Example:

# def greet():
#     name = "Skyler"
#     print(f"Hello, {name}!")

# # test inside a function
# greet()
# Hello, Skyler!   # output

# # test outside a function
# print(name)        
# Error: NameError - name is not defined  # Errors out

# Here, name only exists within the greet() function. After greet() finishes, 
# name is removed from memory therefore throwing an error saying that ‘name’ is not defined.


# Why Scope and Lifetime Matter
# Avoid Errors: Prevents accidental use of variables that don’t exist in the current scope.
# Organized Code: Helps structure code by keeping variables only where they’re needed.
# Efficient Memory Use: Local variables are discarded after use, freeing up memory.


# Practice Exercises
# Exercise 1: Local and Global Variables
# Write a function favorite_food() that prints your favorite food stored in a 
# local variable called food. Then, create a global variable food and set it to something else. Print both to observe the scope difference.
# food = "Pizza"   # Global variable

# def favorite_food():
#     food = "Sushi"   # Local variable
#     print("Local food:", food)

# favorite_food()              # Prints: Local food: Sushi
# print("Global food:", food)  # Prints: Global food: Pizza



# Exercise 2: Variable Lifetime in Functions
# Define a function counter() that initializes a local variable count to 0 
# and increments it by 1 each time counter() is called. Print count after each call and observe the results.
# def counter():
#     count = 0      # Local variable
#     count += 1
#     print("Count:", count)

# counter()          # Prints: Count: 1
# counter()          # Prints: Count: 1


# Each call to counter() reinitializes count to 0 due to the local scope of count.

# Exercise 3: Combining Scope and Lifetime
# Create a program where you have a global variable user_name set to your name. 
# 
# Inside a function change_name(), create a new local variable also named user_name, 
# but set it to something else. Print both user_name variables (inside and outside the function) 
# to see the effect of scope on variable values.
# user_name = "Skyler"   # Global variable

# def change_name():
#     user_name = "sfines"  # Local variable
#     print("Inside function:", user_name)

# change_name()                         # Prints: Inside function: sfines
# print("Outside function:", user_name) # Prints: Outside function: Skyler

# The local user_name inside change_name() does not affect the global user_name.


# Modules in Python

# MODULES
# Definition: A module is a Python file that contains code you can reuse in other 
# parts of your project. Modules help in organizing related functions, classes, and v
# ariables together so that your code becomes more structured and easier to manage.

# Key Concepts:
# Built-in Modules: Python comes with many built-in modules, such as math, random, and
# datetime, which provide a wide range of functionalities
# .Example:
# import math
# print(math.sqrt(16))  
# 4.0  # output

# In this example, the math module provides a function sqrt() to calculate the square root 
# of a number. We can use this instead of writing our own function.

# Custom Modules: You can create your own modules by writing reusable functions in separate
# Python files and importing them into your main script.
# Example:
# Step 1: Create a file called greetings.py with the following content:
# def say_hello(name):
#     return f"Hello, {name}!"


# Step 2: Now, in another file, in the same directory, import and use the custom module:
# import greetings
# print(greetings.say_hello("Skyler")) 
# Hello, Skyler!  # output

# This greetings.py file can be used as a module in any other python script you have by importing it.
# Note: The filename for modules should end in .py.



# WHY USE MODULES?

# Code Reusability: Modules allow you to write code once and use it multiple times, saving time and effort.

# Organized Structure: Keeping related functions in separate files helps keep your project clean and easy to understand.

# Easier Maintenance: If you need to make changes, you only need to update the module,
# which reflects the changes everywhere it’s used.

# Example: Imagine you have a function to calculate tax in multiple scripts. 
# Instead of rewriting the function each time, you can create a module called tax_calculator.py 
# and import it wherever you need it. This reduces redundancy and makes future updates easier.





# HOW TO IMPORT MODULES
# Import the Entire Module:
# import random
# print(random.randint(1, 10))  # Prints a random number between 1 and 10

# This imports all functions and variables from the random module. You need to specify the 
# name of the module followed by the name of the function using dot notation ‘.’ to make 
# this work. In this example, the function randint comes from the random module so we call
# it by using: random.randint(parameter1, parameter2)

# Import Specific Functions or Variables:
# from math import pi, sqrt

# print(pi)
# 3.141592653589793   # output

# print(sqrt(25))
# 5.0   # output

# Only the specified items (pi and sqrt) are imported, making the code easier to read. 
# In this case, you can only use ‘pi’ and ‘sqrt’. If you need to use other functions 
# living under math, you have to explicitly import those as well. 
# Using Aliases:
# import os as o  # we use alias o instead of os

# # Example using os.getcwd() to get the current working directory
# current_directory = o.getcwd()
# print(current_directory)
# # Output
# # The current working directory (e.g., '/home/user/projects')

# Aliases can make module names shorter, simplifying code writing.
# Creating and Importing Modules

# To create your own modules, you simply write Python code in a separate file and then import it.
# Creating Module A:
# Step 1: Create a new file called module_a.py. 
# Write a simple function inside module_a.py named ‘welcome’:
# def welcome():
#     print("Welcome to Module A!")


# Creating Module B:
# 	Step 2: Create another file called module_b.py.
# Import module_a in module_b and call the function:
# import module_a

# def call_module_a():
#     print("Calling Module A from Module B")
#     module_a.welcome()

# # run
# call_module_a()

# # output
# Calling Module A from Module B
# Welcome to Module A!

# When you run module_b.py, you will see the messages from both modules, showing how one module 
# can call functions from another.

# SPECIAL MODULE CONCEPTS
# Key Concepts:
# if __name__ == "__main__": This line is used to control when certain parts of your code should run.
# This makes sure that the code we want to execute only executes if the file is being run directly.
# It prevents code from  running if we want to use a python file as a module but still allows us to
#  execute the code in this file if needed.
# # In a file named example.py
# def example_function():
#     print("This is an example function.")

# if __name__ == "__main__":
#     example_function()

# if we remove the line if __name__ == "__main__":, when we import example.py into another module,
# it will execute example_function() automatically even if we don't want it to.  Here’s why:
# In Python, every script has a special built-in variable called __name__. This variable helps
# determine how the script is being used.
# When you run the script directly by running python example.py in the terminal, Python 
# sets the variable __name__ to the value "__main__". This tells Python that this is the 
# main program being executed. You can test this by running this in your script:
# # Example: example.py
# print(__name__)  # This will print: __main__

# When you import the script as a module into another file, Python sets __name__ to the name 
# of the file/module, in this case, the value would be “example”. Because the condition 
# requires __name__ to have the value “__main__”, it won’t run the code automatically.

# __init__.py: This file is used to mark a directory as a Python package. This allows you 
# to group related modules together. Although it became optional in Python 3.3+, it’s still 
# commonly used to initialize packages and manage what gets imported when a package is imported.


# Practice Exercises
# Exercise 1: Create a Custom Module: 
# Follow the instructions above and create module_a.py and module_b.py. Try running the 
# commands mentioned on your own. Add functions in module_a and try calling them in module_b.

# Exercise 2: Import Specific Functions
# From the datetime module, import the date class and print today’s date.
# from datetime import date
from datetime import date
print(date.today())
# print(date.today())  # Prints today's date, e.g., 2024-11-10


# Exercise 3: Applying special module concepts:
# Modify the code you have in module_a so that it runs the function welcome() only when 
# you directly execute it (won't automatically run if you import it onto module b).















