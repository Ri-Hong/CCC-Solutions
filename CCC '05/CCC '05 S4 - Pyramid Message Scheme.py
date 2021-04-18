'''
Author: Ri Hong
Date AC'd: Jan 27, 2021
Problem: https://dmoj.ca/problem/ccc05s4
'''

#Explanation
"""
1. We need a structure to store the tree(the connection of people). I have chosen to use a dictionary with the superior as the key
and the subordinates in a list as the value. The way we build this structure is that we loop through the names of people while
keeping track of the previous name and if the current person is not in the tree yet, then we add them as the subordinates of the 
previous person. If they are in the tree, then it means that it was returning to a superior and we don't need to do anything with it.

2. The old messaging time can be found easily by multiplying the number of messages(which is given to us) by 10, since it 
takes 10s to send each message.

3. To find the new messaging time, we want to find the height of the tree not including the sender/"home"(aka how many levels of 
subordinates there are). For example, the sample input has a height of 2: Alfred and Betty are on the first level and Cindy and 
Dennis are on the second. Note that the height of the tree is equivalent to the maximum amount of times a message needs to be 
sent downwards to subordinates. We multiply the height by two because the message needs to be returned back to the root and then 
multiply by 10s per message to get the improved message sending time. 

4. From there, subtract the new time from the old time to get the time saved.

NOTES: 1. The function for finding height of tree is called bfs(breadth first search) because that is essentially how the new
messaging system works: send a message to all the subordinates then wait for a respose instead of sending one message at a time 
and waiting for a respose before sending the message to the next subordinate. The old method is similar to a DFS(depth first search).
You can read up on BFS and DFS here if you are interested: https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/ 

      2. This question is structured a bit strangely in that the beginning person/root is not consistent. For example, the sample
input uses "Home" as the root, but the test cases do not always use "Home" as the root. However, you can find the root if you 
first take the list of people as input and then look at the last person. The last person is gaurenteed to be the root because the
message has to end up back at the root. This is why I had to get all the input first, put it in a list, then build the tree instead
of what I would usually do which is, get each person and build the tree one person at a time.
"""

#Code
def bfs(tree, root): #this will calculate the new time required to send the messages and return the new time
  heightOfTree = 0 #stores the height of the tree (aka how many levels of subordinates there are)
  currentRecipiantList = [root] #this will store all the recipiants on the same "level/height". Initialized to the root

  while True: #loop
    nextRecipiantList = [] #create/clear a new list for the next batch of recipiants
    isEnd = True #stores if we are at the end of the tree. Initialize it to true at the beginning

    for currentRecipiant in currentRecipiantList: #for all the current recipiants in the current recipiant list
      if len(tree[currentRecipiant]) != 0: #if the list of the current recipiant's subordinates is not empty, the we have not reached the end of the tree
        isEnd = False 
        nextRecipiantList.extend(tree[currentRecipiant]) #add all the recipiants of the current recipiant to the next recipiant list

    if isEnd == True: #if we are at the end of the tree, then we can exit the loop
      break
    else: #if we are not at then end of the tree, we and add one to the height of the tree and set the currentRecipiantList to the people in the nextRecipiantList
      heightOfTree += 1
      currentRecipiantList = nextRecipiantList

  #once we are done traversing down the tree, we will know the height of the tree. 
  #Then we multiply by 2 because once a message reches the depth of the tree, it has to return back up to the root. 
  #Multiply by 10 because it takes 10s to send each message
  return heightOfTree * 2 * 10
#-----------------MAIN-----------------

numMessageLists = int(input()) #get the # of message lists

for i in range(numMessageLists): #for each message list:
  numMessages = int(input()) #get the number of messages
  oldMessagingTime = numMessages * 10 #stores the old messaging time. Calculated by number of messages * 10s per message
  tree = {} #this will store the tree(the connection of people) 
  #The values represent the direct subordinates of each superior (key) 
  #E.G. {"Alfred": ["Cindy", "Dennis"]} means that Cindy and Dennis are the suborinates of Alfred
  #Structure: {From1 : [to1, to2, to3...], From2 : [to1, to2, to3...]...}

  messageList = [] 
  for j in range(numMessages): #loop through the number of messages
    messageList.append(input()) #get the name of the person and put it in the messageList
  root = messageList[-1] #set the root as the last entry
  tree[root] = [] #give root a list for its subordinates
  previousPerson = root #this will store the previous person we received as input. Initialize to root

  for currentPerson in messageList: #loop through each Person in the list
    if currentPerson not in tree.keys(): #if the person is not already in the tree, then they must be the subordinate of the previous person
      tree[previousPerson].append(currentPerson) #add the person as the subordinate of the previous person
      tree[currentPerson] = [] #make the current Person a new list for their own subordinates if they end up having any

    previousPerson = currentPerson #make the current person the previous person before we go onto the next iteration of the for loop


  newMessagingTime = bfs(tree, root)
  timeSaved = oldMessagingTime - newMessagingTime
  print(timeSaved)