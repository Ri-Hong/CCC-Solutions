'''
Author: Ri Hong
Date AC'd: Feb 15, 2021
Problem: https://dmoj.ca/problem/ccc17j4
'''

#Code
#Set constants
time = [12,00] #set time
count = 0 #set count 
d = int(input()) #collect input

#Values for if it goes beyond 12h
factor = d//1440  #determine the number of days (repeats)
d -= (d//1440)*1440 #Take away those repeats

#MAIN LOOP
for d in range (d+1): #set the the amount of mins it will go through
#Set Variables
  difference = []  #set list
  num = []  # set list
  A = False #set atrithmetic to false

#Correct the format
  if d >=60: #correct time if mins > 60
    h = d//60
    d = d % 60
    time[0] = h
    if time[0] > 12: #correct time if hours > 12
      time[0] -= 12
  
#Make digits into int to better calculate
  if d < 10:  #if mins are single digits, correct the format and make str
    time[1] = '0' + str(d) 
  else:
    time[1] = str(d) 
  ttime = str(time[0]) + time[1] #make string so it's easier to deal

  for i in range (len(ttime)): #add each number into a list and turn into int for calulations
    num.append(int(ttime[i]))

#Compare differences
  for i in range (len(num)-1):  #Calculate the differences and use to compare later
    difference.append(num[i+1] - num[i])

  for i in range (len (difference)-1):  #compare differences to check
    if difference[i] == difference [i+1]:
      A = True #continue if true
    else:
      A = False #If differences are different, break the loop
      break

  #Add to count
  if A == True: #check if it ends up true, then add towards the count
    count +=1

#Output results
print (count + factor*62)#Add count with the factor and the constant from a 24h period