'''
Author: Ri Hong
Date AC'd: Mar 1, 2021
Problem: https://dmoj.ca/problem/ccc21s3
'''

#Explanation
'''
***Note that this solution only ACs when Pypy 3 is selected as the language on DMOJ instead of Python 3

SUBTASK 1
For the first subtask, we can use linear search to find our answer.
Step 1
Loop through all possible positions from the leftmost friend to the rightmost friend. This position will be our supposed concert location. The reason we only have to loop from the leftmost friend to the rightmost friend
is because the further left you start a concert to the left of the leftmost friend, the more time it would take all friends to walk there. Suppose the leftmost friend is at position 5. Supose you host the concert at position 4
instead of position 5. Now every friend needs to walk at most one step left to be able to hear the concert. The same reasoning applies to the right boundary and the rightmost friend. That is why we only have to search between
the leftmost friend and the rightmost friend, since searching beyond the people on the end is garunteed not to produce a more optimal walking time for all the friends.

Step 2
For each concert location, calulate how much time it would take all friends to be able to hear the concert and store it in a list

Step 3 
From the list, choose the smallest value. That is the smallest amount of time it would take every friend to hear the concert.

For example, following sample input # 3, we can see that there are friends at locations 1, 6 and 14, so we have to search all values from 1 to 14 inclusive. 
If the concert was a position 1, then walking time 
= time it takes the person at position 1 to get to position 1 + time it takes the person at position 6 to get to position 1 + time it takes the person at position 14 to get to position 1
= 0 + 2m * 8s/m + 11m * 5s/m
= 0 + 16s + 55s
= 71s
Put this value into the list: [71]
If the concert was a position 2, then walking time 
= time it takes the person at position 1 to get to position 2 + time it takes the person at position 6 to get to position 2 + time it takes the person at position 14 to get to position 2
= 0 + 1m * 8s/m + 10m * 5s/m
= 0 + 8s + 50s
= 58s
Put this value into the list: [71, 58]

Continue to do this until you finish processing position 14. Then you sould have a list that looks like:
[71, 58, 49, 48, 47, 46, 45, 44, 43, 50, 57, 64, 76, 88, 43]

We can look through the list and see that the minimum value is 43, so 43 is the minimum amount of seconds it would take everyone to reach a particular concert.

SUBTASK 2-3
For the rest of the subtasks, instead of performing a linear search through the possible positions, we can perform binary search instead. If you do not know what binary search is, feel free to seach it up. 
Step 1
We have a left/lower boundary and a right/higher boundary. The starting left boundary would be the position of the leftmost person. The concert position we search is always going to be at the center of the left
and right boundary. 

Step 2
At that concert position, we want to again compute how long it takes every friend to walk within hearing distance of the concert. Next we want to check the positions directly to the left and right of our current concert position.
We want to check if hosting the concert to the left or right of the concert position will result in a smaller walking time for all our friends, so we have to again compute how long it takes every friend to walk within hearing 
distance of the concert if the concert was at current concert position - 1 and current concert position + 1. 

If moving the concert to the left will produce a smaller walking time, then we want to adjust the right boundary to be the current concert position
If instead moving the concert to the right will produce a smaller walking time, then we want to adjust the left boundary to be the current concert position
If neither moving the concert to the left or to the right produces a more optimal walking time than our current position, then we have found the position that requires the least total walking time from all our friends.

We want to keep performing step 1 and 2 until we find the most optimal position.
'''

#Code
#Note, you might want to read the main code before the function

#calculates the total time it takes every friend to be able to hear the concert given the position of the concert
def calculateTime(concertPosition):
  totalTime = 0 #stores the total time it takes every friend to walk to be able to hear the concert
  for friend in friends: #loop through every friend
    #give each variable a more meaningful name
    position = friend[0]
    speed = friend[1]
    hearingStrength = friend[2]

    #left position and right position stores the positions at which a friend must walk to to be able to hear the concert
    leftPosition = concertPosition - hearingStrength
    rightPosition = concertPosition + hearingStrength
    if position in range(leftPosition, rightPosition + 1): #check if the friend can already hear the concert
      continue

    distanceAway = min(abs(position - leftPosition), abs(position - rightPosition)) #calculate the distance that the friend must walk
    totalTime += distanceAway * speed #calculate the time it takes the friend to walk that distance

  return totalTime #return the total time it takes for all friends to be able to hear the concert


#---MAIN---
friends = [] #will become a 2D array. Structure: [[Pi, Wi, Di],[Pi, Wi, Di]...]. The friends array stores a number of friend arrays. Each friend array has the friend's position, speed, and hearing distance in that order. E.g. for sample input 3, the array would be [[6, 8, 3], [1, 4, 1], [14, 5, 2]]

numFriends = int(input())

#boundaries are used for binary search. Init to extreme low and high numbers so that it is garunteed that they will have a value later on
rightBoundary = 0 
leftBoundary = 1000000000

for i in range(numFriends): #loop through each friend
  #get the position, speed, and hearingStrength of each friend and put it in the friends array
  position, speed, hearingStrength = list(map(int, input().split()))
  friends.append([position, speed, hearingStrength])

  #check if the boundaries need to be updated
  if position > rightBoundary:
    rightBoundary = position
  if position < leftBoundary:
    leftBoundary = position


#binary search
while True: #keep looping until an optimal position is found

  concertPosition = int((rightBoundary + leftBoundary)/2) #set teh concert position to be the middle of the left and right boundaries
  currentTime = calculateTime(concertPosition) #calculate the time it takes for every friend to be able to hear the concert

  #check which direction we should go in next
  if calculateTime(concertPosition - 1) < currentTime: #if going left is more advantageous
    rightBoundary = concertPosition #decrease the right boundary
  elif calculateTime(concertPosition + 1) < currentTime: #if going right is more advantageous
    leftBoundary = concertPosition #increase the left boundary
  else: #if staying at our current position is more advantageous than going left or right
    break #exit the loop. We have found out optimal concert position

print(currentTime) 