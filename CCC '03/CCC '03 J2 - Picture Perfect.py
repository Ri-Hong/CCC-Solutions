'''
Author: Ri Hong
Date AC'd: Jan. 31, 2020
'''

#Explanation
'''
Given an area, the shape that results in the smallest perimeter is a square. That means that we want to arrange the photos in as much of a square shape as possible.
In other words, if we have two dimensions for the arrangement, a and b, we want the values of a and b to be as close together as possible. Keep in mind that a X b = 
the number of photos in the arangement. If the number of photos is a perfect square, then a and b will both be the square root of that number, as that's the closest
a and b can be. For example, if the number of photos is 100, then a = b = root(100) = 10. Given this fact, we can start searching for valid factors starting from the
square root of the number of photos and ending at 1. The first factor that we find will be a and b will be: number of photos/a.
'''

#Code
from math import sqrt #import the square root function from the math library

while True: #keep looping to get input
  numberOfPhotos = int(input()) #get the number of photos as an integer
  if numberOfPhotos == 0: #if the number of photos is 0, we can exit the loop and end the program
    break

  for dimension1 in range(int(sqrt(numberOfPhotos)), 0, -1): #loop through the possible values for dimension1 ranging from the square root of the number of photos to 1. Remember to int() the square rooted result as it may not be an integer
    if numberOfPhotos % dimension1 == 0: #if dimension 1 is a factor of the number of photos
      dimension2 = int(numberOfPhotos/dimension1) #calculare dimension 2
      perimeter = dimension1 * 2 + dimension2 * 2 #calculate the perimeter
      print("Minimum perimeter is {} with dimensions {} x {}".format(perimeter, dimension1, dimension2)) #print the result
      break #exit the for loop. No need to look for a second dimension for the same number of photos

