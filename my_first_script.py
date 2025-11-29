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


# def print_grocery_list_items(grocery_list, nice_to_have_list=None):
#     print("We need to buy the following: ")
#     for item in grocery_list:
#         print(item) 

#     if nice_to_have_list:
#         # ‘\n’ means new line. So this will add a blank line
#         print("\nIf possible, it would be nice to buy the following as well:")
#         for item in nice_to_have_list:
#             print(item)



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
# from datetime import date
# print(date.today())
# # print(date.today())  # Prints today's date, e.g., 2024-11-10


# # Exercise 3: Applying special module concepts:
# # Modify the code you have in module_a so that it runs the function welcome() only when 
# # you directly execute it (won't automatically run if you import it onto module b).


# # ==========================================================================
# # Day 6: Core PEP 8 Rules and Best Practices
# WHAT IS PEP 8?
# Definition: PEP 8 is Python's official Style Guide for Python Code. It outlines conventions to make Python code consistent, readable, and professional. Whether you're collaborating with a team or revisiting your own work, following PEP 8 ensures your code is clean and easy to understand.
# Think of it as a set of rules for writing Python that not only makes your work look polished but also helps prevent common mistakes. Today, we’ll focus on some key PEP 8 principles, including indentation, line length, blank lines, and import organization.


# INDENTATION
# Indentation refers to the spaces at the beginning of a line of code that visually and syntactically define blocks of code in Python. For example, blocks in functions, loops, or conditionals must be indented to show that they belong together. Python enforces indentation as part of its syntax.

# Rule: Use 4 spaces per indentation level. Avoid tabs.

# Why it Matters: 
# Indentation makes your code visually structured and ensures Python understands the hierarchy of your logic.
# Using spaces instead of tabs avoids inconsistencies in how different editors display your code.

# How to Set in VSCode:
# Go to File > Preferences > Settings.
# Search for "insert spaces".
# Check the option for "Insert Spaces".




# LINE LENGTH
# Line length refers to the maximum number of characters allowed on a single line of code. Python’s PEP 8 recommends keeping lines at 79 characters or fewer.

# Rule: Limit each line of code to 79 characters or fewer.

# Why it Matters:
# Makes code easier to read, especially on smaller screens or during side-by-side reviews.
# Prevents long lines from becoming overwhelming or difficult to follow.

# How to Add a Visual Ruler in VSCode:
# Go to your settings

# Search for Rulers and click on the settings.json file

# Edit this line
# "editor.rulers": [79]

# Save



# BLANKLINES (WHITESPACE)
# Blank lines are intentional gaps between lines of code that visually separate sections. They act like paragraph breaks in writing, making your code easier to read and follow.

# Rules:
# Use two blank lines between top-level functions or classes.
# Use one blank line between methods inside a class.

# Why it Matters:
# Blank lines make it easy to identify different parts of your code, like functions, classes, or logical sections.
# They improve readability and maintain a clean structure.




# ORGANIZING IMPORTS
# Imports bring external modules and libraries into your program, allowing you to use their functions and tools. PEP 8 specifies guidelines for the placement and organization of imports.

# Rules:
# Place imports at the top of the file.
# Follow this order:
# Standard library imports (e.g., import os).
# Third-party imports (e.g., import numpy).
# Local imports (e.g., import core).
# Alphabetize imports within each group.
# Avoid wildcard imports (e.g., from module import *).

# Why it Matters:
# Organized imports clarify which libraries are used in your code.
# Separating imports into groups helps collaborators quickly locate dependencies.
# Alphabetizing imports improves consistency and readability.

# How to Automate in VSCode:
# Install the isort extension to automatically organize imports.





# Identifying Standard vs. Third-Party Modules
# How do I know if a module is part of the standard library or a third-party library?
# Standard Library:
# Modules that come bundled with Python by default (e.g., os, sys, math).
# Check the Python Standard Library documentation to confirm.
# Third-Party Library:
# Modules or packages installed via package managers like pip (e.g., numpy, requests).
# Typically found in the site-packages directory of your Python installation.

# Feature
# Standard Library
# Third-Party Library
# Comes with Python
# Yes
# No (must be installed with pip)
# Found in Standard Docs
# Yes (Python Standard Library)
# No
# Examples
# os, sys, datetime, math
# numpy, pandas, requests
# Location in Python Path
# /lib/pythonX.X (Standard folder)
# /site-packages folder


# Practice Exercises
# Exercise 1: Indentation
# Fix the indentation in this code
def potatoes():
    print("Potatoes!")
    print("Boil 'em, mash 'em, put 'em in a stew")


# Exercise 2: Line Length
# Rewrite this line to respect the 79-character limit.
# long_string = "This is an example of a very long string that goes well beyond" \
# " the character limit."


# # Exercise 3: Blank Lines
# # Add the appropriate blank lines. 
# class Example:
#     def first_method(self):
#         pass
#     def second_method(self):
#         pass

# def function_a():
#     print("It’s too cramped!")
    
# def function_b():
#     print("I need some space!")

#Day 6: Naming Conventions and Whitespace

# Naming Conventions
# Consistent naming conventions help others instantly understand your code. A good name communicates the purpose of a variable, function, or class without needing extra explanation.
# Rules:
# Variables and Functions:
# Use snake_case: lowercase letters with underscores separating words.
# Example: my_variable, calculate_sum().
# Classes:
# Use CapWords (PascalCase): Each word starts with a capital letter, no underscores.
# Example: MyClass, UserAccount.
# Constants:
# Use ALL_CAPS: All letters uppercase with underscores separating words.
# Example: MAX_LIMIT, TAX.
# Why This Helps:
# Makes it easy to distinguish between types of identifiers.
# Ensures a consistent style that everyone can follow.



# Whitespace
# Whitespace makes your code visually organized and easier to read. Misplaced or inconsistent spaces can make code confusing and hard to follow.

# Rules:
# Add spaces around operators like +, -, *, = for clarity:
# Example: result = (a + b) * (c - d) (Correct)
# Avoid: result=(a+b)*(c-d) (Incorrect)
# Avoid unnecessary spaces:
# Inside parentheses, brackets, or braces:
# Example: my_list = [1, 2, 3] (Correct)
# Avoid: my_list = [ 1, 2, 3 ] (Incorrect)
# Around keyword arguments:
# Example: func(arg=42) (Correct)
# Avoid: func(arg = 42) (Incorrect)
# Tools:
# Use a tool like Black Formatter in VSCode to automatically handle proper spacing.
# Black formatter can be found in extensions




# Practice Exercises
# Exercise 1: Naming Conventions
# Fix the naming in this code snippet and rewrite using proper naming conventions.
# def CalculateSum(a, b):
#     totalsum = a + b
#     return totalsum


# # Exercise 2: Whitespace
# # Add the correct whitespace to this code.
# result=(a + b ) * (c - d)
# my_list = [1,2, 3]
# print (result)

# Day 6: Documentation and Comments

# Why Documenting Your Code Matters
# Good documentation clarifies what your code does, explains why decisions were 
# made, and helps others (and your future self) quickly understand and 
# modify your code.

# Inline Comments
# Purpose: Explain why something is done, not just what is happening.

# Best Practices:
# Keep them short and focused.
# Place them above or next to the relevant line of code.
# Avoid obvious comments like # Set value to 5.

# Example:
# # Initialize base value for calculations
# value = 5



# Docstrings
# Purpose: Provide context for functions, classes, or modules.

# Best Practices:
# Explain what the function/class/module does.
# List input parameters and their types.
# Describe the return value and its type.

# Here is an example of a Google style docstring:
# def add_numbers(x, y):
#     """
#     Adds two numbers.

#     Args:
#         x (int): The first number.
#         y (int): The second number.

#     Returns:
#         int: The sum of x and y.
#     """
#     return x + y



# How to Set Up autoDocstring in VS Code
# Step 1: Install autoDocstring

# In VS Code go to the Extensions Marketplace (Ctrl+Shift+X or Cmd+Shift+X).
# Search for "autoDocstring" and click Install.

# Step 2: Configure for Google Style (optional)

# The best style for docstrings largely depends on your team’s preferences, 
# the project’s complexity, and the tools you’re using.

# Why Use Google Style?
# Google style is highly readable, even for beginners.
# Many tools, including autoDocstring, Sphinx, and IDEs like PyCharm and VS Code,
# support Google style.
# Ideal for teams that use mixed environments or want consistent documentation.
# Works well in Markdown-like outputs and renders cleanly in documentation 
# generators like Sphinx.
# The structure is intuitive and less verbose than NumPy style, making it easy 
# for teams new to documentation to adopt.

# Open your VS Code settings:
# Navigate to File > Preferences > Settings (Windows/Linux)
# Code > Preferences > Settings (Mac).
# Search for autoDocstring.DocstringFormat.
# Select google as the value

# Practice Exercises
# Exercise 1: Inline Comments
# Write inline comments explaining why each step is performed in the following 
# code:
# def separate_fruits_and_veggies(items):# defining the function
#     fruits = [] # blank list created 
#     veggies = []
#     for item in items: # iterate over the list
#         name, category = item #parameters to be iterated over
#         if category == 'fruit': # loop to check for item match
#             fruits.append(name) # add to fruits list if item is found
#         else:
#             veggies.append(name) # if item not found in fruits list will 
# add to
#             # veggies list
#     return fruits, veggies # return values


# Exercise 2: Docstrings
# Using the same code, write a docstring. Make sure it explains what the 
# function does, lists parameter inputs and their types, and the return values 
# and their types.

#======================Day 6: Organization and Modularity ========================================================
# Organizing and breaking down your code into manageable, modular pieces isn’t
#  just about making it look nice—it’s crucial for usability, maintenance, and
#  scalability. Clean and modular code is easier to debug, reuse, and share 
# with others. Let’s dive into the principles that will help you write 
# better-organized Python code.

# Single Responsibility Principle (SRP)
# Purpose: Ensure that each function or module does one thing and does it well.

# Best Practices:
# Avoid cramming everything into one function
# Each function should do one thing

# Non-SRP Example:
# def make_sandwich(bread, fillings, condiments):
#     # Gather ingredients
#     ingredients = [bread]
#     ingredients.extend(fillings)
#     ingredients.extend(condiments)
    
#     # Assemble the sandwich
#     sandwich = f"{ingredients[0]} with " + ", ".join(ingredients[1:])
    
#     # Serve the sandwich
#     print(f"Here is your sandwich: {sandwich}")

# bread = "Whole grain"
# fillings = ["Turkey", "Cheese"]
# condiments = ["Mayo", "Mustard"]
# make_sandwich(bread, fillings, condiments)



# SRP Example:
# # Responsibility 1: Gather ingredients
# def gather_ingredients(bread, fillings, condiments):
#     ingredients = [bread]  # Start with the bread
#     ingredients.extend(fillings)  # Add all fillings
#     ingredients.extend(condiments)  # Add all condiments
#     return ingredients

# # Responsibility 2: Assemble the sandwich
# def assemble_sandwich(ingredients):
#     sandwich = f"{ingredients[0]} with " + ", ".join(ingredients[1:])
#     return sandwich

# # Responsibility 3: Serve the sandwich
# def serve_sandwich(sandwich):
#     print(f"Here is your sandwich: {sandwich}")

# # Main function that coordinates the process
# def make_sandwich(bread, fillings, condiments):
#     # Pass the ingredients as arguments
#     ingredients = gather_ingredients(bread, fillings, condiments)
#     sandwich = assemble_sandwich(ingredients)
#     serve_sandwich(sandwich)

# bread = "Whole grain"
# fillings = ["Turkey", "Cheese"]
# condiments = ["Mayo", "Mustard"]

# # Call the main function
# make_sandwich(bread, fillings, condiments)



# Keep Functions Short
# Purpose: Improve readability and ease of debugging.

# Best Practices:
# If a function exceeds 20 lines, think about how to break it into smaller, 
# focused functions.

# Group Related Functions and Constants
# Purpose:  Keep your code logical and easy to navigate.
# Group file-related operations in one file/module (e.g., file_operations.py).
# Keep constants for file paths or settings together in a constants.py file.

# constants.py example:
# TAX = 0.12  # Default Tax Amount

# # Error Messages
# ERROR_ITEM_NOT_FOUND = "Error: Item not found in inventory."
# ERROR_INVALID_QUANTITY = "Error: Invalid quantity provided."

# # Application Metadata
# APP_NAME = "Grocery List App"
# VERSION = "1.0.0"
# AUTHOR = "Skyler Fines"

# # Categories (for grouping items)
# CATEGORIES = ["Fruits", "Vegetables", "Dairy", "Meat", "Beverages"]

# # Inventory Defaults
# DEFAULT_RESTOCK_QUANTITY = 10  # Amount to restock when items are low
# DEFAULT_ITEMS = {
#     "apples": 10,
#     "bananas": 8,
#     "oranges": 2,
# }


# Use a Top-Down Approach
# Purpose: Help readers understand the high-level structure before diving 
# into details.
# Place the main logic at the top of the script and helper functions below.

# Main Functions: These functions orchestrate the overall logic of the program.
#  They call helper functions to perform specific tasks, handle the program's
#  flow, and interact with the user (e.g., getting input or displaying output).

# Helper Functions: These are smaller, modular functions designed to perform 
# specific, often repetitive, tasks. They "help" the main functions by 
# handling the details of certain operations, making the main function cleaner
#  and easier to read.

# # Main function
# def manage_shopping_cart():
#     """Main function to manage the shopping cart."""
#     items = ["Banana", "Apple", "Carrot"]
#     prices = [0.99, 1.49, 0.79]
    
#     sorted_items = sort_list(items)  # Calls helper function
#     total_cost = calculate_total_cost(prices)  # Calls helper function
    
#     print("Shopping Cart:")
#     for item, price in zip(sorted_items, prices):
#         print(f"{item}: ${price:.2f}")
#     print(f"Total Cost: ${total_cost:.2f}")

# # Helper functions
# def sort_list(items):
#     """Sort a list of items."""
#     return sorted(items)

# def calculate_total_cost(prices):
#     """Calculate the total cost of items."""
#     return sum(prices)

# # Run the main function
# manage_shopping_cart()

# Tip: ZIP


# Example:
# # Two lists to zip
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# # Using zip
# zipped = zip(list1, list2)

# # Converting the result to a list
# print(list(zipped))


# Expected Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]



# Encapsulate Data and Methods in Classes
# Purpose:  Bundle related data and methods to improve modularity and 
# organization.
# We will explore classes and methods further into the course.

# Example:
# class GroceryList:
#     def __init__(self):
#         """Initialize an empty grocery list."""
#         self.items = []  # Data: A list to store grocery items

#     def add_item(self, item):
#         """Add an item to the grocery list."""
#         pass

#     def remove_item(self, item):
#         """Remove an item from the grocery list if it exists."""
#         pass

#     def edit_item(self, old_item, new_item):
#         """Edit an item in the grocery list."""
#         pass

#     def list_items(self):
#         """Display all items in the grocery list."""
#         pass


# *Note: Here we are only using pass in these methods to so it is easier to 
# see the big picture


# Practice Exercises
# Practice Code:
# def make_taco():
#     # Choose the taco type
#     taco_type = input("What kind of taco are you making? 
# (e.g., Chicken, Beef, Veggie): ")
    
#     # Gather ingredients
#     ingredients = []
#     while True:
#         ingredient = input("Enter an ingredient (or 'done' to stop): ")
#         if ingredient.lower() == 'done':
#             break
#         ingredients.append(ingredient)
    
#     # Assemble and display the taco
#     print(f"\nAssembling your {taco_type} taco with the following 
# ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")
#     print(f"\nYour {taco_type} taco is ready! Enjoy!")

# make_taco()


# Exercise 1: Break Down the Function (SRP)
# Refactor the make_taco function into three smaller functions:
# A function to choose the taco type.
# A function to gather ingredients.
# A function to assemble and display the taco.

# Suggested tasks:
# A function for adding items to the list.
# A function for calculating the total cost.
# A function for printing the grocery list and total cost.

# Exercise 2: Use a Helper Function
# Create a helper function to format the ingredient strings (e.g., "- Beef").
#  Use this helper function inside the taco assembly function. 

# Example:
# def format_ingredient(ingredient):
#     new_ingredient = f"- {ingredient}"
#     return new_ingredient


# Exercise 3: Top Down Approach
# Organize your code so the main functions are at the top and helper functions
#  are at the bottom.

# Exercise 4: Grouping Related Functions
# Create a new module called taco_maker.py and add your code in here. This way
#  only taco making code lives here. 

# Exercise 5: Apply PEP 8
# Apply PEP 8 rules to the taco_maker module. Add in-line comments and a 
# docstring.



# Exercise 6: BONUS - ZIP
# You are making tacos, and you have two lists:
# A list of toppings for the taco (e.g., "Lettuce", "Cheese", "Salsa").
# A list of quantities for each topping (e.g., "1 cup", "1/2 cup", "2 tbsp").
# Change these values to your own preferences

# Write a function using zip to combine these two lists into a single list of 
# strings, where each string describes a topping and its quantity. 
# Finally, print each topping and its quantity.
# Hint: for topping, quantity in toppings_with_quantities:

# Example Input:
# toppings = ["Lettuce", "Cheese", "Salsa"]
# quantities = ["1 cup", "1/2 cup", "2 tbsp"]


# Example Output:
# - Lettuce: 1 cup
# - Cheese: 1/2 cup
# - Salsa: 2 tbsp

#Day 6: Error Handling with LBYL and EAFP
# Errors can cause your program to crash, frustrating users and disrupting workflows. Proper error handling ensures your program can deal with unexpected situations gracefully.

# Look Before You Leap (LBYL)
# This approach involves checking conditions before performing an operation.

# When to Use LBYL:
# When pre-checking is quick and straightforward.
# To prevent predictable errors like accessing an item in a grocery list dictionary that might not exist.

# Example:
# grocery_list = {"apples": 5, "bananas": 3, "milk": 2}

# # LBYL approach
# if "eggs" in grocery_list:
#     print(f"Eggs: {grocery_list['eggs']} units")
# else:
#     print("Error: 'eggs' not found in the grocery list.")



# Easier to Ask for Forgiveness than Permission (EAFP)
# This approach skips pre-checks and handles errors if they occur.

# When to Use EAFP:
# When errors are rare or unpredictable.
# When working with uncertain operations, like fetching an item from the grocery list.

# Example:
# grocery_list = {"apples": 5, "bananas": 3, "milk": 2}

# # EAFP approach
# try:
#     print(f"Eggs: {grocery_list['eggs']} units")
# except KeyError:
#     print("Error: 'eggs' not found in the grocery list.")

# # Call the main function
# make_sandwich(bread, fillings, condiments)


# LBYL and EAFP
# LBYL:
# Proactive: Checks before acting.
# Ideal for predictable scenarios.
# Provides more control over your code and looks more professional.
# EAFP:
# Reactive: Acts first and handles issues if they arise.
# Useful for scenarios with rare or unpredictable errors.
# Allows for flexibility when testing new code


# Practice Exercises
# grocery_list = {"bread": 4.50, "cheese": 12.47, "yogurt": 3.99}


# Exercise 1: LBYL and EAFP
# Given the above grocery list:
# Write a script that gets the value of “butter”. 
# This will raise a KeyError since “butter” is not in the dictionary.
# Solve the KeyError using LBYL
# Solve the KeyError using EAFP

#==========================================================


#Day 6: Multi-Line Text, Comments, and F-Strings
# Understanding how to manage multi-line text, comments, and complex 
# expressions is essential for writing clean, readable, and maintainable Python 
# code. Long lines of code or text can quickly become unwieldy, leading to bugs 
# and confusion. By mastering these concepts, you’ll learn how to organize your
#  code effectively—an invaluable skill for any developer.
# Let’s break this down step by step with practical examples to guide you along
#  the way!

# Multi-Line Strings
# When dealing with long pieces of text, Python provides two simple methods to
#  keep everything tidy: parentheses and triple quotes.

# Using Parentheses
# If you’re working with a long string, you can wrap it in parentheses to split
#  it across multiple lines without introducing syntax errors.

# Example:
# long_string = (
#     "If we put out text in parenthesis"
#     "We can write multi-line strings"
#     "This saves us space and keeps things clean"
# )
# print(long_string)


# Output:
# If we put out text in parenthesisWe can write multi-line stringsThis saves 
# us space and keeps things clean

# When using parenthesis, if we want the text to appear on separate lines like
#  it is displayed instead of on one line, we need to explicitly use the escape
#  sequence \n

# Example with Escape Sequence:
# long_string = (
#     "If we put out text in parenthesis\n"
#     "We can write multi-line strings\n"
#     "This saves us space and keeps things clean\n"
# )
# print(long_string)




# Output:
# If we put out text in parenthesis
# We can write multi-line strings
# This saves us space and keeps things clean


# Using Triple Quotes
# For text that needs to maintain its exact formatting, triple quotes are your
#  go-to.

# Example:
# long_string = """
# Triple quotes give us more control:
# 1. The text output will appear as is
# 2. This makes it more predictable
# 3. Making it easier to maintain formatting
# """
# print(long_string)


# Output:
# Triple quotes give us more control: 
# 1. The text output will appear as is
# 2. This makes it more predictable   
# 3. Making it easier to maintain formatting



# Multi-Line Function Calls
# When working with functions that take several parameters, it’s best to place
#  each argument on a new line to improve readability.

# Example:
# # Long Function Call
# add_item(name="Kiwis", store="Costco", cost=10.50, amount=2, priority=2,
#  buy=True)

# # Multi-Line Function Call
# add_item(
#     name="Kiwis",
#     store="Costco",
#     cost=10.50,
#     amount=2,
#     priority=2,
#     buy=True
#     )


# This structure makes it easier to scan and debug functions, especially 
# when the arguments are complex.






# Multi-Line Data Structures
# Large data structures like lists, dictionaries, and sets benefit from being 
# split across lines.

# Lists
# # Long List
# grocery_items = ["Apples", "Bananas", "Carrots", "Dates", "Eggplants", 
# "Potatoes", "Chocolate", "Cake"]

# # Multi-Line List
# grocery_items = [
#     "Apples",
#     "Bananas",
#     "Carrots",
#     "Dates",
#     "Eggplants",
#     "Potatoes",
#     "Chocolate",
#     "Cake"
#     ]


# Dictionaries
# # Long Dictionary 
# grocery_item = {"name": "chicken", "store": "Walmart", "cost": 12.57, 
# "amount": 2, "priority": 1, "buy": True}

# # Multi-Line Dictionary 
# grocery_item = {
#     "name": "chicken",
#     "store": "Walmart",
#     "cost": 12.57,
#     "amount": 2,
#     "priority": 1,
#     "buy": True
#     }





# Multi-Line Comments
# Triple quotes are often used as a workaround for multi-line comments. 
# Though they are technically multi-line strings, Python ignores them if they 
# are not assigned to a variable.

# Example:
# """
# This is a multi-line comment.
# It spans several lines.
# Use triple quotes for this purpose.
# """
# print("Code runs normally.")

# These are also often used as module docstrings

# Note: If placed inside a function or class, triple quotes are interpreted 
# as docstrings and not comments.

# Another way is to use the # symbol on each line of the comment. This 
# approach is explicit and avoids confusion.

# # This is a multi-line comment.
# # It uses the # symbol for each line.
# # This method is more explicit.

# print("Code runs normally.")


# Which Method Should You Use?
# Use triple quotes if the comment is long and spans multiple lines, and it 
# won’t be confused with a docstring (e.g., outside of functions or classes).
# Use # for shorter or standard multi-line comments, as it’s explicit and 
# fits Python’s conventions.✅
# Module Docstrings
# A module docstring is a special kind of docstring that appears at the very 
# top of a Python file. It provides a high-level overview of the module's 
# purpose, functionality, and any additional information helpful for users or 
# developers working with the module.

# Why Use Module Docstrings?
# To explain what the module does.
# To document the module's functionality and usage.
# To provide metadata, such as author information, version, or licensing.

# How to Write a Module Docstring
# Place the docstring as the very first statement in the Python file 
# (before imports or code).
# Use triple quotes (""" or ''') to enclose the docstring.
# Include concise but informative details.

# Example:
# """
# grocery_list_core.py

# This module provides the core functionality of the app.
# It includes features for adding, removing, and editing items.

# Functions:
# - add_item(): Adds an item to the list.
# - remove_item(): Removes an item from the list.
# - edit_item: Edit an existing item from the list.

# Author: Skyler Fines
# Version: 1.0.0
# """



# Practice Exercises
# Exercise 1: Multi-Line String
# Write three things about yourself in a string variable called about_me.
# Copy the variable and break it into three lines using parenthesis
# Copy the variable and break it into three lines using triple quotes
# Both outputs should look the same
# Example:
# "I work in QA, I love hiking, and I have a pet cat."


# Exercise 2: Multi-Line Function Call
# The following function call is too long and does not comply with PEP 8 
# guidelines because of its length. 
# Rewrite it by placing each parameter on a new line.
# add_bee_hive(beekeeper_name="Alice", location="North Field", 
# hive_capacity=50, bee_species="Apis mellifera", honey_production_rate=20.5,
#  hive_health="Good", queen_present=True, last_inspection="2024-11-20", 
# notes="Hive thriving with high activity")


# Exercise 3: Multi-Line Data Structures
# You are given a dictionary with 10 stores and their inventory numbers 
# written as a single line.
# Rewrite it so each store and its inventory count is on a new line for 
# better readability.
# stores = {"Store A": 120, "Store B": 340, "Store C": 275, "Store D": 420,
#  "Store E": 310, "Store F": 95, "Store G": 240, "Store H": 180, 
# "Store I": 60, "Store J": 410}




# Exercise 4: Module Docstring
# You’re creating a Python module for a Bee Keeper Management App. Write 
# a module docstring based on the following details:
# Name: bee_keeper_manager.py
# Purpose: To help beekeepers manage their hives, track honey production,
#  and monitor hive health.
# Features:
# Add new hives.
# Update hive health status.
# Track honey production rates.
# Generate hive activity reports.
# Author: Buzz McComb
# Version: 2.1

#====================================================================================

# Day 6: Avoiding Global Variables and Using Constants
# Understanding how to manage variables effectively is crucial for writing reliable, maintainable, and scalable code. Global variables, while convenient, can work unpredictability and make debugging difficult. This document will guide you through the importance of avoiding global variables and how to use constants effectively to enhance code clarity and maintainability. By the end, you'll have a solid understanding of these concepts and practical exercises to reinforce them.

# Why Avoid Global Variables?
# Global variables are accessible from anywhere in your code. While this might seem helpful, it creates challenges:
# Harder Debugging: Tracking where a global variable was changed can be difficult, especially in larger projects.
# Unpredictable Behavior: Global variables can be unintentionally modified by different parts of the program, leading to bugs.
# Reduced Code Readability: It’s harder to understand the scope and purpose of global variables.



# Best Practices
# Pass Variables as Arguments
# Instead of relying on global variables, pass the required values directly to functions.

# Example:
# def multiply_by_two(num):
#     return num * 2

# # Instead of number being a global variable
# # We assign it here
# number = 10
# result = multiply_by_two(number)
# print(result)  # Output: 20


# Encapsulate Variables in Functions or Classes
# Keep variables local to their specific function or class to limit their scope.

# Example:
# def calculate_area(length, width):
#     area = length * width  # 'area' is local to this function
#     return area

# length = 5
# width = 10
# result = calculate_area(length, width)
# print(result)  # Output: 50





# Using Constants
# We have already touched on constants and earlier modules, but this might be a good review.

# Constants are variables that should not change throughout the program. Python uses a naming convention of ALL_CAPS to identify constants.
# Benefits:
# Enhances code readability.
# Makes updates easier (change in one place updates all references).
# Reduces hardcoding and duplication.

# Example:
# MAX_CONNECTIONS = 5 # ALL CAPS shows the reader these values will not change
# TIMEOUT_DURATION = 30

# def connect():
#     for i in range(MAX_CONNECTIONS):
#         print("Connecting...")


# Constants should always be found at the top of the file

#=============================================================

# Day 6: Type Hints and Annotations
# Type hints are a valuable addition to Python that make code easier to understand, maintain, and debug. In this module, you’ll learn how to use type hints and annotations effectively to improve your code’s clarity and quality.

# What Are Type Hints?
# Type hints allow you to specify the expected types of arguments, return values, and variables in your code.
# They don’t enforce type rules at runtime but serve as helpful guides for developers and tools like linters.
# A linter is a tool that analyzes your code for potential errors, stylistic inconsistencies, and violations of coding standards. 
# Introduced in Python 3.5, they are not supported in older Python versions.



# Function Annotations
# Function annotations let you define the types of inputs and outputs for functions.
# Type hints are part of function annotations, specifically used for defining the types of arguments and return values.
# Function annotations can also serve other purposes but are most commonly used for type hints.

# Function Annotation Example:
# def add(x: int, y: int) -> int:
#     return x + y


# Function Annotation vs Type Hints
# When we are throwing around terms like type hints and function annotations their definitions and usage can sound the same. Let’s clear that up:

# Function Annotation:
# In Python, any metadata attached to a function’s parameters or return value using the : or -> syntax is a function annotation.
# In this case, x: int, y: int, and -> int are function annotations because they describe additional information about the function.

# Type Hint:
# The specific information provided by the annotations (int for x and y, and int for the return type) is a type hint.
# Type hints are a specific use case of function annotations, indicating the types of inputs and outputs expected for the function.





# Function Annotations VS Type Hints
# You can use : and -> in function annotations for purposes other than type hints by attaching arbitrary metadata to function parameters and return values.

# When Would You Do This? (IF YOU’RE CURIOUS)
# To add contextual information about parameters or return values directly in the code, especially when generating auto-documentation.
# Generating auto-documentation means using tools to automatically extract and organize information from your codebase to create comprehensive, human-readable documentation.
# Tools like sphinx, pdoc, Doxygen, Pydoctor
# If you have a custom tool or decorator that interprets these annotations to validate inputs dynamically. (We’ll learn about decorators later)

# Example (function annotation that is not a type hint):
# def save_file(file_path: "Must be a valid file path"):
#     pass


# For specialized applications, such as scientific computing, where annotations could describe units, ranges, or assumptions.

# Example (function annotation using descriptive metadata):
# def convert_temperature(temp: "Celsius value", target_unit: "Fahrenheit or Kelvin") -> "Converted temperature":
#     return temp * 9/5 + 32 if target_unit == "Fahrenheit" else temp + 273.15


# Frameworks like Flask or Django could use function annotations to register routes or describe APIs.


# Variable Type Hints
# Type hints can also be used with variables to specify the type of data they should hold.
# name: str = 'Python'
# age: int = 33
# is_active: bool = True


# name is expected to be a string, age an integer, and is_active a boolean.

# Benefits of Type Hints
# Improves Code Readability: Makes it clear what types are expected without extra comments.
# Helps Catch Errors Early: Tools like mypy can detect mismatches during development.
# Supports Collaboration: Makes it easier for others to understand and work with your code.

# Limitations
# Type hints are not enforced by Python at runtime.
# Older Python versions (before 3.5) don’t support type hints, so consider compatibility if you’re working in a shared or legacy environment.


# Complex Variable Type Hints
# Some type hints might be a bit more complex than a single type. Let’s use our grocery list variable for example:


# Here we have a list
# Within that list there are dictionaries
# Within each dictionaries there are more variable types
# grocery_list = [
#     {"name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True},
#     {"name": "bread", "store": "Walmart", "cost": 4.50, "amount": 2, "priority": 1, "buy": True}
# ]


# Here we can specify the list with the list type then square brackets [ ]
# Then we specify that the elements of the list are dictionaries dict[ ]
# Each dictionary has:
# Key Type: str (keys are strings).
# Value Type: A union of float, int, str, and bool (values can be any of these types).
# grocery_list: list[dict[str, float | int | str | bool]] = [
#     {"name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True},
#     {"name": "bread", "store": "Walmart", "cost": 4.50, "amount": 2, "priority": 1, "buy": True}
# ]

# Note that you don't specify the type for each individual key (e.g., name, store). Instead, the type hint applies once to all keys and once to all values in the dictionary.

# So the type hint looks like this:
# grocery_list: list[dict[str, float | int | str | bool]]



# Also note that the syntax for complex type hints can be slightly different based on the python version.

# For example python 3.9 or earlier doesn’t support the | operator. 

# For Python 3.10+: list[dict[str, float | int | str | bool]]
# For Python < 3.10: List[Dict[str, Union[float, int, str, bool]]]

# Practice Exercises
# Exercise 1: Add Type Hints to a Function
# Update the following function to include type hints for the parameters and the return value.
# Hint: The parameter name should be a string, and the function should return a string.

# Function:
# def apples(apple_type):
#     return f"I love, {apple_type} apples!"


# Exercise 2: Use Type Hints for Variables
# Rewrite the code below to include type hints for the variables.
# Hint: Use str for title, int for years_experience, and bool for is_remote.

# Variables:
# title = "Python Developer"
# years_experience = 10
# is_remote = True


# Exercise 3: Annotate a Math Function
# Add type hints to this function, which calculates the area of a rectangle.
# Hint: length and width should be float, and the return value should also be float.

# Function:
# def calculate_area(length, width):
#     return length * width


























