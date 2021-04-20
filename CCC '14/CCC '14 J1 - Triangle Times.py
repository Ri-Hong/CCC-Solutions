'''
Author: Ri Hong
Date AC'd: Jan 5, 2020
Problem: https://dmoj.ca/problem/ccc14j1
'''

#Explanation
'''
Get the three angles. If they add up to 180, then we have to further check if the triangle is isosceles, equalateral or scalene.
If the angles don't add up to 180, then output "Error"
'''
#Code
#Get side lengths
a = int(input())
b = int(input())
c = int(input())
#Check if the sides add up to 180
if a + b + c = 180:
  if a = 60 and b = 60 and c = 60: #Equilateral
      print("Equilateral")
  elif a not= b and b not= c and c not= a: #Scalene
      print("Scalene")
  elif (a = b and a not= c) or (a = c and a not= b) or (b = c and b not= a): #Isosceles
      print("Isosceles")
else:
  print("Error")