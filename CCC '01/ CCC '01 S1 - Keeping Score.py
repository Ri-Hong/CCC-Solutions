'''
Author: Ri Hong
Date AC'd: Feb. 2, 2020
'''

#Explanation
'''
Step 1
Convert the string of cards into 4 lists which hold the cards for each suit. 

Strp 2
Then for the cards in each suit, we calculate the total point value of them. 
First we check the number of cards in each suit. If a suit has 0 cards, then it is a void: +3 points, 1 card = singleton: +2 points, 2 cards = doubleton: +1 point.
Then check each card to see if it is an ace, king, queen or jack and if it is, we add the corresponding point value. 

Step 3
Now we have to format the output. First we print the headers, Cards Dealt and Points
Then we print the name of each suit with a the list of cards in that suit separated with spaces. On the same line, we print the point total for that suit.
On the last line, we print "Total" and the total point value.

Note that the our output does not need to exactly match the sample output in the problem statement. The spacing between the Cards Dealt column and the Points column
is completely up to you. For example, even though the output for sample test case 1 was:
Cards Dealt              Points
Clubs 2 5 8 T J K             4
Diamonds 6 9 Q A              6
Hearts                        3
Spades T J A                  5
                       Total 18

This output would still be accepted:
Cards Dealt Points
Clubs  2 5 8 T J K 4
Diamonds  6 9 Q A 6
Hearts  3
Spades  T J A 5
Total 18
'''



#calculates the point value of a given set of cards
def pointCalculator(suitList): #suitList is a list that holds each card of a suit
  totalPoints = 0 #keeps track of the point total so far for all the suits. Initialized to 0
  if len(suitList) == 0: #void
    totalPoints += 3
  elif len(suitList) == 1: #singleton
    totalPoints += 2
  elif len(suitList) == 2: #doubleton
    totalPoints += 1

  for card in suitList: #loop through each card and check if it holds value
    if card == "A": #if the card is an ace, add 4 points
      totalPoints += 4
    elif card == "K": #if the card is a king, add 3 points
      totalPoints += 3
    elif card == "Q": #if the card is a queen, add 2 points
      totalPoints += 2
    elif card == "J": #if the card is a jack, add 1 points
      totalPoints += 1
  return totalPoints #return the total point value of the suit


hand = input() #read the set of 13 cards as a string
#thsese following lists store the cards in each suit. E.g. CList stores the cards of the suit clubs. DList stores the cards of the suit diamonds
CList = []
DList = []
HList = []
SList = []

#loop through the hand. Once a suit identifier is found (C, D, H, S), add all the cards beweeen it and the next suit identifier
for i in range(1, hand.index("D")):
  CList.append(hand[i])
for i in range(hand.index("D")+1, hand.index("H")):
  DList.append(hand[i])
for i in range(hand.index("H")+1, hand.index("S")):
  HList.append(hand[i])
for i in range(hand.index("S")+1, len(hand)):
  SList.append(hand[i])

#format the list of cards in each suit for output. It will be a string composed of the card names seperated by spaces
CListFormatted = ""
for i in range(len(CList)):
  CListFormatted = CListFormatted + " " + CList[i]

DListFormatted = ""
for i in range(len(DList)):
  DListFormatted = DListFormatted + " " + DList[i]

SListFormatted = ""
for i in range(len(SList)):
  SListFormatted = SListFormatted + " " + SList[i]

HListFormatted = ""
for i in range(len(HList)):
  HListFormatted = HListFormatted + " " + HList[i]

#calculate the total number of points of the cards
totalPoints = pointCalculator(CList) + pointCalculator(DList) + pointCalculator(HList) + pointCalculator(SList)

#deal with output
print("Cards Dealt", "Points") #print the header

#print the clubs row
print("Clubs", CListFormatted, end = " ") 
print(pointCalculator(CList))

#print the diamonds row
print("Diamonds", DListFormatted, end = " ")
print(pointCalculator(DList))

#print the hearts row
print("Hearts",HListFormatted, end = " ")
print(pointCalculator(HList))

#print the spades row
print("Spades",SListFormatted, end = " ")
print(pointCalculator(SList))

#print the total number of points
print("Total", totalPoints)