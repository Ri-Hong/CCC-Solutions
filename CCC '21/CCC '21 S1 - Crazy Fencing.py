'''
Author: Ri Hong
Date AC'd: Feb 17, 2020
Problem: https://dmoj.ca/problem/ccc21s1
'''

#Explanation
'''
For each piece of wood, the area is w * (h1 + h2)/2, where w represents the width, h1 represents the first height (left height) and h2 represents the second height (right height).
For example, in the diagram for sample input 1, when looking at the first piece of wood, w = 4, h1 = 2, h2 = 3 (note that h1 and h2 can be swapped).
'''

#Code
nWood = int(input()) #get the number of pieces of wood as an integer

heights = list(map(int, input().split())) #gets the heights as a string, splits it into a list, and casts each value into an integer
widths = list(map(int, input().split())) #gets the widths as a string, splits it into a list, and casts each value into an integer

area = 0 #stores the area of the entire fence
for i in range(len(widths)): #loop through each of the widths by index
  area += widths[i] * (heights[i] + heights[i+1])/2 #calculate area of each piece of wood. A = w * (h1 + h2)/2

print(area) #print the final area