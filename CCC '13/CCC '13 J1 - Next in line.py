'''
Author: Ri Hong
Date AC'd: Jan 4, 2020
Problem: https://dmoj.ca/problem/ccc13j1
'''

#Explanation
'''
Get the age of the youngest and middle child. The difference can be found by subtracting the youngest child's age from the 
middle child's age. Then to get the oldest child's age, add the difference to the middle child's age.
'''
#Code
youngest = int(input())
middle = int(input())
oldest = middle + middle - youngest
print(oldest)