#I used option 2
total_cost_list = [] #list of price of items in user's order
final_order_list = [] #list of items in user's order
type_list = [] #list of types of items in user's order, used in the order function
print("Welcome!")
def menu():
  print("What would you like to order?\n  1: Sandwich\n  2: Drink\n  3: French Fries\n  4: Ketchup Packets\n  5: Check Out")
  welcome = int(input("Please enter the number corresponding with the item you would like. (1, 2, 3, 4, or 5)"))
  #asks the user what they would like to add to their order, then the if-elif statement below calls the corresponding function depending on what the user added to their order
  if (welcome == 1):
    sandwich()
  elif (welcome == 2):
    drink()
  elif (welcome == 3):
    fries()
  elif (welcome == 4):
    ketchup()
  elif (welcome == 5):
    order()
def sandwich():
  sandwich_list = ["Chicken Sandwich", "Beef Sandwich", "Tofu Sandwich"]
  price_list = [5.25, 6.25, 5.75]
  #lists of avaliable sandwiches and prices
  print("\nChoose between the following sandwiches:\n  1: Chicken ($5.25)\n  2: Beef ($6.25)\n  3: Tofu ($5.75)")
  index = input("Please select the number of the sandwich you would like to purchase! (1, 2, or 3)")
  #asks the user what sandwich they would like
  if (index == "1" or index == "2" or index == "3"):
    index = int(index)
    print("You picked a " + sandwich_list[index - 1] + " for $" + str(price_list[index - 1]))
    #tells the user what they added to their order
    total_cost_list.append(price_list[index - 1])
    #adds the sandwich price to the total cost list
    final_order_list.append(sandwich_list[index - 1])
    #adds the sandwich to the final order
    type_list.append(1)
    #adds the sandwich to the type list
    cost()
    #calls the cost function, tells the user what is in their order so far
  else:
    print("Please enter a valid response!")
    sandwich()
def drink():
  drink_list = ["Small  Drink", "Medium Drink", "Large Drink"]
  price_list = [1, 1.75, 2.25]
  #lists of avaliable drink sizes and prices
  print("Which size would you like?\n  1: Small ($1)\n  2: Medium ($1.75)\n  3: Large ($2.25)")
  index = input("Please select the number of the drink size you would like to purchase! (1, 2, or 3)")
  #asks the user what drink size they would like
  if (index == "1" or index == "2" or index == "3"):
    index = int(index)
    print("You picked a " + drink_list[index - 1] + " for $" + str(price_list[index - 1]))
    #tells the user what was added to their order
    total_cost_list.append(price_list[index - 1])
    #adds the drink price to the total cost list
    final_order_list.append(drink_list[index - 1])
    #adds the drink to the final order
    type_list.append(2)
    #adds the drink to the type list
    cost()
    #calls the cost function, tells the user what is in their order so far
  else:
    print("Please enter a valid response!")
    drink()
def fries():
  frie_list = ["Small Fries", "Medium Fries", "Large Fries", "Mega-sized Fries"]
  price_list = [1, 1.50, 2, 2]
  #lists of avaliable fries sizes and prices
  print("\nWhich size would you like?\n  1: Small ($1)\n  2: Medium ($1.50)\n  3: Large ($2)")
  index = input("Please select the number of the frie size you would like to purchase! (1, 2, or 3)")
  #asks the user what size fries they would like
  if (index == "1" or index == "2" or index == "3"):
    index = int(index)
    if (index == 1):
      print("Would you like to mega-size your fries?\n  1: Yes\n  2: No")
      mega = input("Please enter 1 or 2 for yes or no.")
      #if they ordered a small, asks them if they would like to mega-size their order
      if (int(mega) < 2):
        index = 4
        #if they answer yes, mega-size their order
    print("You picked a " + frie_list[index - 1] + " drink for $" + str(price_list[index - 1]))
    #tells the user what was added to their order
    total_cost_list.append(price_list[index - 1])
    #adds the fries price to the total cost list
    final_order_list.append(frie_list[index - 1])
    #adds the fries to the final order
    type_list.append(3)
    #adds the fries to the type list
    cost()
    #calls the cost function, tells the user what is in their order so far
  else:
    print("Please enter a valid response!")
    fries()
def ketchup():
  print("Ketchup: $0.25 each")
  index = int(input("How many ketchup packets would you like?"))
  #asks how many ketchup packets the user wants
  print("You added " + str(index) + " ketchup packets for $" + str(index * 0.25) + ".")
  #tells the user what was added to their order
  total_cost_list.append(index * 0.25)
  #adds the ketchup cost to the total cost list
  final_order_list.append(str(index) + " Ketchup Packets")
  #adds the ketchup to the final order lsit
  type_list.append(4)
  #adds ketchup to the type list
  cost()
def order():
  length = len(final_order_list) #checks how many items the user is ordering
  cost = 0 #initialize cost variable
  finalCost = 0 #initialize final cost variable
  combo = 0 #initialize combo variable
  index = 0 #intitialze index variable
  sandwich = 0 #initialize sandwich variable
  drink = 0 #initialize drink variable
  fries = 0 #initialize fries variable
  itemNumber = 1 #initialize itemNumber variable
  while (index < length): #runs the following code for each item ordered
    if (type_list[index] == 1):
      sandwich = sandwich + 1
      #if the item is a sandwich, adds 1 to the sandwich variable
    elif (type_list[index] == 2):
      drink = drink + 1
      #if the item is a drink, adds 1 to the drink variable
    elif (type_list[index] == 3):
      fries = fries + 1
      #if the item is fries, adds 1 to the fries variable
    cost = cost + total_cost_list[index]
    #adds the cost of the item  to the cost variable
    print("  " + str(itemNumber) + ": " + final_order_list[index] + ", $" + str(total_cost_list[index]))
    #prints the item and it's cost
    index = index + 1 #updates index variable
    itemNumber = itemNumber + 1 #updates itemNumber variable
  index = 0 #resets index variable
  while (index < length): #runs the following code for each item ordered
    if (sandwich > 0 and drink > 0 and fries > 0):
      #checks if there is a sandwich, drink, and fries in the order
      sandwich = sandwich - 1 #updates sandwich variable
      drink = drink - 1 #updates drink variable
      fries = fries - 1 #updates fries variable
      combo = combo + 1 #updates combo variable
    index = index +1 #updates index variable
  finalCost = cost - combo #sets the finalCost to the cost - the combo
  print("Your order cost is: $" + str(cost) + "\nYour combo discount is: $" + str(combo * 1) + "\nYour final price is: $" + str(finalCost))
  #tells the user their cost, combo discount, and final cost
def cost():
  cost = 0 #initialize cost variable
  length = len(final_order_list) #checks how many items the user is ordering
  index = 0 #initialize index variable
  print("\nYour order so far:")
  while (index < length):
    #for each item in the order, adds the cost to the cost variable and tells the user what the item is and how much it costs
    cost = cost + total_cost_list[index]
    print("  - " + final_order_list[index] + ", $" + str(total_cost_list[index]))
    index = index + 1 #updates the index variable
  menu() #allows the user to add more items to their order
menu()