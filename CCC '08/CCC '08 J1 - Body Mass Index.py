'''
Author: Ri Hong
Date AC'd: Jan 31, 2020
Problem: https://dmoj.ca/problem/ccc08j1
'''

#Explanation
'''
Get the width and height and calculate BMI using the formula: BMI = weight/height^2
'''
#Code
#Get input
weight = float(input())
height = float(input())
BMI = weight / height**2 #Calculate BMI
#Output the appropriate message
if BMI >= 25:
  print("Overweight")
elif BMI >= 18.5 and BMI <= 25:
  print("Normal weight")
else:
  print("Underweight")