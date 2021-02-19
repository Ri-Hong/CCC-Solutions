'''
Author: Ri Hong
Date AC'd: April 30, 2020
'''
#Explanation
'''
Basiclly, this question is asking you to find the maximum distance between two elements of two lists
A "distance" is defined as the difference between the indexes of the two lists where the larger index needs 
also carry a value that is larger or equal to the value of the index of the other list
If we have a list named X with index i and another list named Y with index j. Then the maximum distance would
be the maximum possible value of j - i with the constraint that Y[j] >= X[i]
'''

#get the number of test cases as an integer
numTestCases = int(input())
for i in range(numTestCases): #loop through each testcase
  numElements = int(input()) #get the length of the lists as an integer
  #get the lists and convert them to a form where list1 stores the values as an integer.
  #i.e. go from a string of 1 2 3 4 5 to a list of [1, 2, 3, 4, 5]
  list1 = list(map(int, input().split()))
  list2 = list(map(int, input().split()))

  #find greatest distance
  greatestDist = 0 #initialize the greatestDistance to be 0
  for i in range(len(list1)): #loop through list1
    for j in reversed(range(len(list2))): #loop through list2 in reverse
      if list2[j] >= list1[i]: #if the value of the current index of list 2 is greater than the value of the current index of list 1
        dist = j - i #calculate the difference
        if dist > greatestDist: #check if the difference is greater than the greatest distance
          greatestDist = dist #if it is, assign the difference as the new greatest distance

  #print out the answer
  print("The maximum distance is %d"%greatestDist)