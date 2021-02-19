'''
Author: Ri Hong
Date AC'd: Jan. 28, 2020
'''
#Explanation
'''
First we get the amount of quarters Martha starts with and the number of times each machine has been played since it last paid.
Next we simulate Martha playing each machine until she runs out of quarters. We also keep track of the number of times she plays.
For each play on a machine, we subtract the number of quarters Martha has by 1, increment the number of times Martha has played by 1
and increment the "turn" number of the machine by 1. The "turn" of a machine is how many times it has been played since it last paid out.
Next we check if the the turn is equal to the machine's payout turn. For example, machine 1's payout turn is 35 and machine 2's is 100. 
If it is the payout turn, then Martha gains the amount of quarters the machine pays out(30 for machine 1, 60 for machine 2, 9 for machine 3). 
Then we must reset the machine's turn number to 0, since it just paid out. Finally, we check if Martha is out of quarters, if she is, then we
exit the loop and output how many times she can play before she goes broke.
'''

#Code
#Get input
startingQuarters = int(input()) #get the number of quarters Martha starts with as an integer
machine1Turn = int(input()) #get the number machine 1 has been played since it last paid as an integer
machine2Turn = int(input()) #get the number machine 2 has been played since it last paid as an integer
machine3Turn = int(input()) #get the number machine 3 has been played since it last paid as an integer

marthaplayNumber = 0 #stores the number of times Martha has played. Initialized to 0
#simulate the plays
while startingQuarters > 0: #keep looping as long as Martha still has quarters left
    #simulate playing machine 1
    startingQuarters -= 1 #subtract 1 quarter in order to play machine 1
    machine1Turn += 1 #increment the turn of machine 1 by 1
    marthaplayNumber += 1 #increment the number of times martha played by 1
    if machine1Turn == 35: #if the machine is on turn 35
        startingQuarters += 30 #martha gains 30 more quarters
        machine1Turn = 0 #reset the machine's turn to 0
    if startingQuarters <= 0: #check if Martha is out of quarters
        break #if so, exit the while loop
    
    #simulate playing machine 2
    startingQuarters -= 1 #subtract 1 quarter in order to play machine 2
    machine2Turn += 1 #increment the turn of machine 2 by 1
    marthaplayNumber += 1 #increment the number of times martha played by 1
    if machine2Turn == 100: #if the machine is on turn 100
        startingQuarters += 60 #martha gains 60 more quarters
        machine2Turn = 0 #reset the machine's turn to 0
    if startingQuarters <= 0: #check if Martha is out of quarters
        break #if so, exit the while loop

    #simulate playing machine 3
    startingQuarters -= 1 #subtract 1 quarter in order to play machine 3
    machine3Turn += 1 #increment the turn of machine 3 by 1
    marthaplayNumber += 1 #increment the number of times martha played by 1
    if machine3Turn == 10: #if the machine is on turn 10
        startingQuarters += 9 #martha gains 9 more quarters
        machine3Turn = 0 #reset the machine's turn to 0
    if startingQuarters <= 0: #check if Martha is out of quarters
        break #if so, exit the while loop

#print out the number of times Martha can play before going broke
print("Martha plays", marthaplayNumber, "times before going broke.")