'''
Author: Ri Hong
Date AC'd: Mar 22, 2020
Problem: https://dmoj.ca/problem/ccc17j1
'''

#Explanation
'''
Get the x and y coordinate and compare them to 0 to determine the quadrant the coordinate is in
'''
#Code
a = int(input())
b = int(input())
if a>0 and b>0:
  print("1")
elif a>0 and b<0:
  print("4")
elif a<0 and b<0:
  print("3")
elif a<0 and b>0:
  print("2")