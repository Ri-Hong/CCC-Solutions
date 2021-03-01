'''
Author: Ri Hong
Date AC'd: Feb 18, 2021
Problem: https://dmoj.ca/problem/ccc21s2
'''

#Explanation
'''
The ideology behind this solution is the same as the one in CCC '21 J4 - Arranging Books.py. If you did not read that solution first, I strongly recommend that you do. Also, this solution uses classes, but you can achieve the
same result using variables, just less elegantly (time complexity should be about the same though)
Step 1
Seperate the books into sections
Step 2
Calculate the number of books that can be moved into their section in one swap
Step 3
Deal with the leftover books using # leftovers/3*2

This solution seeks to simplify Step 2 by not actually performing the swaps but using math to achieve the same result. Step 1 is identical. For step 2, instead of actually swapping the books, we can instead calculate
how many books can be swapped. For example, if we wanted to know how many books can be swapped in one move in between the large and small section, we would do: min(numSmallBooksInLargeSection, numLargeBooksInSmallSection).
We would do that for all the 3 pairs of section and add the total up. (L & S, L & M, M & S). 

For step 3, we can find the number of leftovers in a section (the # of books that don't belong in that section) by doing: size of section - number of books beloning to that section - number of swaps made between other sections
For example, if we wanted to find the # of leftovers in the large section, we would do: size of large section - number of Large books - number of swaps made between this section and the medium section -  number of swaps made 
between this section and the small section.
'''

class Section: #stores each section.
  def __init__(self, sectionString):
    #initialize the number of Ls, Ms and Ss in that section
    self.numLs = sectionString.count('L')
    self.numMs = sectionString.count('M')
    self.numSs = sectionString.count('S')
    #initialize the size of the secion
    self.size = len(sectionString)

#---MAIN---
bookOrder = input() #get the order of books initially

#count the number of books of each size
numLs = bookOrder.count('L')
numMs = bookOrder.count('M')
numSs = bookOrder.count('S')

#create each section by giving the Section class the portion of the bookOrder string we want to make a section out of
sectionL = Section(bookOrder[0:numLs])
sectionM = Section(bookOrder[numLs:numLs+numMs])
sectionS = Section(bookOrder[numLs+numMs:])

#calculate the swaps for step 2 (swaps that can place both swapped books in their correct secion in one swap)
lsSwaps = min(sectionL.numSs, sectionS.numLs)
lmSwaps = min(sectionL.numMs, sectionM.numLs)
msSwaps = min(sectionM.numSs, sectionS.numMs)

totalSwaps = lsSwaps + lmSwaps + msSwaps #add up the swaps

#calculate the leftovers for step 3
sectionLLeftovers = sectionL.size - sectionL.numLs - lsSwaps - lmSwaps
sectionMLeftovers = sectionM.size - sectionM.numMs - lmSwaps - msSwaps
sectionSLeftovers = sectionS.size - sectionS.numSs - lsSwaps - msSwaps

totalLeftovers = sectionLLeftovers + sectionMLeftovers + sectionSLeftovers

totalSwaps += int(totalLeftovers/3*2) #add the number of swaps needed to swap the leftover books

print(totalSwaps)