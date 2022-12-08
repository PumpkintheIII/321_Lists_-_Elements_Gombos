#step 5
"""
# a list of menu items
food = ["Burger", "Shake", "Fries"]
first_menu_item = food[0]

print(first_menu_item, "is located at index 0.")
#To access second element of list: 
first_menu_item = food[1]
print(first_menu_item, "is located at index 1.")
#To access third element of list:
first_menu_item = food[2]
print(first_menu_item, "is located at index 2.")
"""

#step 6
"""
# a list of menu items
food = ["Burger", "Shake", "Fries"]

print(food[0], "is located at index 0.")
print(food[1], "is located at index 1.")
print(food[2], "is located at index 2.")
print(food[3], "is located at index 3.")
print(food[-1], "is located at index -1.")
"""

#Boolean Operators and Lists
"""
# a list of menu items
food = ["Burger", "Shake", "Fries"]
#Checks for Burgers:
if ("Burger" in food):
  #Checks to see if the string "Burger" is in the food list
  print("One burger, coming up!")
  #if it is, prints to the terminal saying so
elif ("Burger" not in food):
  #Checks to see if the string "Burger" is not in the food list
  print("Sorry, we don't, have burgers.")
  #if it isn't, prints to the terminal saying so
#This proccess is used for all the other items checked by if statements below
#Checks for Shakes:
if ("Shake" in food):
  print("One shake, coming up!")
elif ("Shake" not in food):
  print("Sorry, we don't, have shakes.")
#Checks for Fries:
if ("Fries" in food):
  print("One fries, coming up!")
elif ("Fries" not in food):
  print("Sorry, we don't, have fries.")
#Checks for Pizza:
if ("Pizza" in food):
  print("One pizza, coming up!")
elif ("Pizza" not in food):
  print("Sorry, we don't, have pizza
"""

#Lists have behaviors, step 14
customer_order = ["Fries", "Shake"] 
#list of items in customer order
item = input("What else would you like to order? ") 
#asks user what item they would like added to their order
customer_order.append(item) 
#adds that item to the customer_order list

print("You ordered", customer_order) 
#prints the order to the terminal
answer = input("Is your order correct? ") 
#asks the user if the order is correct
if (answer == "yes"): 
  #if it is correct, tells the user it is
  print("Great! Your order is coming right up!") 
else: 
  #if it is not correct, allows the user to remove an item
  print("Okay, I will remove", item, "from your order.") 
  customer_order.remove(item) 

print("Your new order is", customer_order)
#tells the user their final order