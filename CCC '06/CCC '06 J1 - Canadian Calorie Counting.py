'''
Author: Ri Hong
Date AC'd: Feb 2, 2020
Problem: https://dmoj.ca/problem/ccc06j1
'''

#Explanation
'''
Get the choice for each type of food item and add it's calorie value to a total
'''
#Code
totalCals = 0 #Stores the total calories
#Handle the calories for the burger
burgerChoice = int(input())
if burgerChoice == 1:
  totalCals += 461
elif burgerChoice == 2:
  totalCals += 431
elif burgerChoice == 3:
  totalCals += 420
elif burgerChoice == 4:
  totalCals += 0

#Handle the calories for the side
sideChoice = int(input())
if sideChoice == 1:
  totalCals += 100
elif sideChoice == 2:
  totalCals += 57
elif sideChoice == 3:
  totalCals += 70
elif sideChoice == 4:
  totalCals += 0

#Handle the calories for the drink
drinkChoice = int(input())
if drinkChoice == 1:
  totalCals += 130
elif drinkChoice == 2:
  totalCals += 160
elif drinkChoice == 3:
  totalCals += 118
elif drinkChoice == 4:
  totalCals += 0

#Handle the calories for the dessert
dessertChoice = int(input())
if dessertChoice == 1:
  totalCals += 167
elif dessertChoice == 2:
  totalCals += 266
elif dessertChoice == 3:
  totalCals += 75
elif dessertChoice == 4:
  totalCals += 0

#Output the total
print("Your total Calorie count is %d." %totalCals)
