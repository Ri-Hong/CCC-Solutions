'''
Author: Ri Hong
Date AC'd: Jan 31, 2020
Problem: https://dmoj.ca/problem/ccc09j1
'''

#Explanation
'''
The first 10 given digits can be stored in a list. Next, get the last 3 digits through input. Then we use a for loop to 
iterate through the list and multiply each number alternatively by 1s and 3s and add up the sum. Then output the sum.

'''
#Code
ISBN = [9,7,8,0,9,2,1,4,1,8] #Stores the first 10 constant digits
#Get the last 3 digits and add them to the list
for i in range(3):
  ISBN.append(int(input()))

sum = 0 #Stores
evenCounter = 0 #Helps keep track of whether the current number should be multiplied by 1 or 3
#Loop through each digit 
for x in ISBN:
  if evenCounter % 2 == 0: #If the even counter is even, we multiply by 1
    sum += x
  else: #If the even counter is odd, we multiply by 3
    sum += x*3
  evenCounter += 1

print("The 1-3-sum is", sum)
