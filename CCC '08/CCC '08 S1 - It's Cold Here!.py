'''
Author: Ri Hong
Date AC'd: Feb 22, 2020
Problem: https://dmoj.ca/problem/ccc08s1
'''

#Explanation
'''
One solution is to store each city and temperature as a key-value pair in a dictionary. Then loop through the dictionary to find
the coldest city.
'''
#Code
cTDict = {} #Stores the cities and temperatures
#Get input and fill in the dictionary
while "Waterloo" not in cTDict: 
  cT = input()
  c, t = cT.split(" ")
  t = int(t)
  cTDict[c] = t
  

coldestTemp = t #Set the coldest temperature to the last temperature for now
#Loop through the dictionary and check if the temperature is lower than the current coldest temperature
for c in cTDict:
  if cTDict[c] < coldestTemp:
    coldestTemp = cTDict[c] #Update the coldest temperature
    coldestCity = c #update the conlest city
    
print(coldestCity)
