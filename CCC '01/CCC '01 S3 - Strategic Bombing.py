'''
Author: Ri Hong
Date AC'd: Feb. 20, 2021
'''

#Explanation
'''
First we create a list of all the roads. Then, we loop through every road and create an adjacency matrix without that specific road. Then
we can use either DFS or BFS to seach through the matrix to see if point A is still connected to point B. If they are disconnected, that means
the road we removed is a disconnecting road. We repeat this process until all roads are checked.
An adjacency matrix is a dictionary where the key is the name/index of a node, and the value is a list of nodes that can be reached from the key node.
For example, 
{
  'A' : ['C', 'D', 'E']
  'C' : ['E', 'F']
}
means that nodes C, D, E are directly connected to node A and nodes E and F are directly conencted to node C.
'''

#searches for a path to get from point A to point B. Returns True if a path exists, False if there is no such path
def DFS(currentPoint): #takes in a parameter currentPoint which is the point we are current at
  if currentPoint == 'B': #if we have reached the destination
    return True #return true

  if currentPoint not in modifiedRoadList.keys(): #if there are no roads leading from this point (dead end)
    return False #return false
    
  returnList = [] #stores a list of return values
  for point in modifiedRoadList[currentPoint]: #loop through all the possible paths connected to our current pount
    if point in visited: #if we have already visited that point
      continue #skip onto the next iteration of the loop
    visited.append(point) #add the point to the visited list
    returnList.append(DFS(point)) #add the result of the DFS call to return list

  if True in returnList: #if there is at leat one True in the return list
    return True #return True (path from A to B exists)
  else: #if there are no Trues in the return list
    return False #return False (path from A to B does not exist)

#builds an adjacency matrix with omitting a selected road
def buildRoadDict(roadNotIncluded): #takes a parameter roadNotIncluded. This is the road that will not be included in the adjacency matrix
  for road in roadList: #loop through all the roads
    if road == roadNotIncluded: #if the road is the road we dont want to include
      continue #move onto the next iteration of the for loop
    start = road[0] #assign the first character of the road as start
    end = road[1]  #assign the second character of the road as end

    if start not in modifiedRoadList.keys(): #if the start node/character is not a key in the adjacency matrix
      modifiedRoadList[start] = [end] #create an entry with the start as the key and the end inside a list as the value
    else: #if the start node already exists as a key in the adjacency matrix,
      modifiedRoadList[start].append(end) #add the end node to the list that has a key of start

    if end not in modifiedRoadList.keys(): #if the end node/character is not a key in the adjacency matrix
      modifiedRoadList[end] = [start] #create an entry with the end as the key and the start inside a list as the value
    else: #if the end node already exists as a key in the adjacency matrix
      modifiedRoadList[end].append(start) #add the start node to the list that has a key of end

#---MAIN---
roadList = [] #stores all the roads
while True: #loop to get all the roads as input
  road = input() #get each road as input
  if road == "**": #if the road is "**", it means it is the last entry, so break
    break
  roadList.append(road) #if the road is anything else, add it to the roadList

disconnectingRoadList = [] #stores the roads that can be bombed in order to prevent travel from point A to B
for removedRoad in roadList: #loop through all the roads
  visited = ['A'] #set the visited list with only 'A' (the start node)
  modifiedRoadList = {} #create an empty dictionary to store the adjacency matrix 
  buildRoadDict(removedRoad) #create the adjacency matrix
  if DFS('A') == False: #check to see if A and B are still connected. If they aern't, that means the current road is a disconecting road
    disconnectingRoadList.append(removedRoad) #add the current road to the disconnectingRoadList

#output
for disconnectingRoad in disconnectingRoadList: #loop through each disconnecting road
  print(disconnectingRoad) #print each disconnecting road
print("There are", len(disconnectingRoadList), "disconnecting roads.") #print the number of disconnecting roads
