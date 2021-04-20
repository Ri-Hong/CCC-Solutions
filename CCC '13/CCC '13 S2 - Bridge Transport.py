'''
Author: Ri Hong
Date AC'd: Sept 1, 2020
Problem: https://dmoj.ca/problem/ccc13s2
'''

#Explanation
'''
We can tackle this problem in two stages. In the first stage, we need to tackle the first 4 cars 1 by 1 just in case the
bridge breaks after one of the first 4 cars is added. If the first 4 cars can make it across the bridge, we will move onto
the second stage, which is checking the rest of the cars until the bridge breaks. We will have a queue of a maximum of 4 
cars at a time that will represent the weights of the cars currently on the bridge. If the total weight exceeds the bridge's
carrying capacity, we can stop the program and output the total. If not, we need to update the queue by removing the first
car and adding the next car and repeating the same process.
'''
#Code
#Get input
maxweight = int(input())
cars = int(input())
carList = []
counter = 0 #Stores the total number of cars that can be driven over the bridge
#Get input and fill up the carList
for i in range(cars):
  weight = int(input())
  carList.append(weight)

checkOtherCars = True #Boolean to store whether we need to handle the rest of the cars after the 4th car
queue = []
#Handle the first 4 cars
for i in range(4):
  queue.append(carList[i]) #Update the list of cars
  if sum(queue) > maxweight: #If the weight limit is exceeded
    print(counter)
    checkOtherCars = False
    break
  else:
    counter += 1

#handle the other cars
if checkOtherCars:
  for i in range(4, cars):
    #Update the list of cars
    queue.pop(0)
    queue.append(carList[i]) 
    if sum(queue) <= maxweight: #If the weight limit is exceeded
      counter += 1
    else:
      break
  print(counter)