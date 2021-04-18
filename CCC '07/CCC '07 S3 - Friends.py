'''
Author: Ri Hong
Date AC'd: May 2, 2020
Problem: https://dmoj.ca/problem/ccc07s3
'''

#Explanation
'''
We can use a dictionary to store each friend connection as a key-value pair. For each set of friends we need to check, we can 
perform a DFS (or BFS) to see if the 2 friends are in the same circle. '''
#Code

import sys
sys.setrecursionlimit(10005) #Since there cannot be more than 9999 friends, we will not allow the program to recurse deeper than 10005 times


gFriendList = {} #Stores all the friends as key value pairs
gCheckingList = [] #A 2D array that stores the pairs of friends that we need to check if they are in a circle

#A recursive function that checks if a rootFriend is in the same circle as a destination friend and returns the distance.
#If the destiantion friend is not in the same circle as the root friend, it returns -1
def inCircle(rootFriend, destinationFriend, currFriend, distance, alreadyVisited):
  alreadyVisited.append(currFriend) #alreadyVisited is an array that stores all the visited friends
  if currFriend == destinationFriend: #If the destination friend is found
    return distance

  if currFriend == rootFriend: #If we have circled back to the first friend
    return -1

  nextFriend = gFriendList[currFriend] #Set the next friend to be the friend of the current friend
  if nextFriend in alreadyVisited: #If the next friend is already visited, return -1
    return -1
  #If the next friend is not visited, call the fucntion again with the next friend as the current friend
  dist = inCircle(rootFriend, destinationFriend, nextFriend, distance+1, alreadyVisited)
  return dist

#------------------main--------------------
numStudents = int(input())
#Get input and construct the gCheckingList
for i in range(numStudents):
  pair = input()
  a, b = pair.split()
  gFriendList[int(a)] = int(b)
while True:
  pair = input()
  a, b = pair.split()
  if a =='0' and b == '0':
    break
  gCheckingList.append([int(a),int(b)])
      
#Loop through each pair we need to check
for i in gCheckingList:
  friendDist = inCircle(i[0], i[1], gFriendList[i[0]], 0, [])
  if friendDist < 0:
    print("No")
  else:
    print("Yes %d"%friendDist)