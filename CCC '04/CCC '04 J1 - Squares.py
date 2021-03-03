'''
Author: Ri Hong
Date AC'd: Jan 5, 2020
Problem: https://dmoj.ca/problem/ccc04j1
'''

#Explanation
'''
Given an area (number of tiles), the side length of the largest square that can be made is the square root of the area. However, the square root of the
might not be an integer, so we have to round it down (floor). The reason we can't round up is because if that happens, then we would not have enough
tiles to fill the entire square.
'''

#Code
import math #import the math library. Used for square root and floor function
numTiles = int(input()) #get the number of tiles we have to work with as an integer
largestSquare = math.floor(math.sqrt(numTiles)) #calculate the largest square side length
print("The largest square has side length {}.".format(largestSquare)) #print the answer