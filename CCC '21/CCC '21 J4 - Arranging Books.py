'''
Author: Ri Hong
Date AC'd: Feb 27, 2021
Problem: https://dmoj.ca/problem/ccc21j4
'''

#Explanation
'''
Step 1
First, we have to split the bookshelf into three sections: the large, medium and small section, where the size of each section is the number of books of that size in the bookshelf.
For example, if the bookshelf order initially was LLLSSM MLLS MLSM, then 
largeSection = [L, L, L, S, S, M] (since there are 6 large books)
mediumSection = [M, L, L, S] (since there are 4 medium books)
smallSection = [M, L, S, M] (since there are 4 small books)

Step 2
Then, we want to swap the books as efficiently as possible. The most efficient swap is if we can swap a book of type A which is currently on shelf B with a book of type B which is currenty
on shelf A. That way, both books will end up in their correct sections with one swap. We would need to swap books from the large and small sections, the large and medium sections and the
medium and small sections to ensure that we have covered all books that can be placed in their correct positions in one move.
Initially the books would look like:
[L, L, L, S, S, M], [M, L, L, S], [M, L, S, M]
Now let's say we first swap the books from the large and small section:
[L, L, L, L, S, M], [M, L, L, S], [M, S, S, M]
Now large with medium:
[L, L, L, L, S, L], [M, M, L, S], [M, S, S, M]
Finally, medium with small:
[L, L, L, L, S, L], [M, M, L, M], [S, S, S, M]

Step 3
Now that we have handled books that can be "completed" in one swap, each set of remaining books can be put into place using 2 swaps.
For example, we could swap the small book in the large section with the medium book in the small section:
[L, L, L, L, M, L], [M, M, L, M], [S, S, S, S]
Then we would swap the medium book in the large section with the large book in the the medium section:
[L, L, L, L, L, L], [M, M, M, M], [S, S, S, S]
Now our books are completely in order. Note that while step 2 needs to actually be implemented (meaning we actually need to build the lists and swap the books), step 3 can be completed
using some basic math. Since each set of remaining books can be put into place using 2 swaps, we can simply take the number of books that are not in place by the end of step 2, divide that by
3 and then multipy by 2 to get the number of swaps needed to get the remaining books into order. For example, there are 3 books out of place in step 2, so 3/3*2 = 2, meaning that by the end of 
step 3, 2 more steps are required to get the last three books into place.

'''

#Code
#READ THE MAIN CODE BEFORE THE FUNCTION PLEASE! :D
#function to swap books. It takes in 2 book sizes and swaps the books from the shelf of bookSize1 to the shelf of bookSize2. Note that this function can only swap books that can be in the correct section in one move.
def swap(bookSize1, bookSize2):
  #assign the appropriate sections to section1 and section2 based on the book sizes
  if bookSize1 == 'L': 
    section1 = sectionL
  elif bookSize1 == 'M':
    section1 = sectionM

  if bookSize2 == 'M':
    section2 = sectionM
  elif bookSize2 == 'S':
    section2 = sectionS

  #count the number of books of size 1 in section 2 and vice versa
  numBookSize1sInSection2 = section2.count(bookSize1)
  numBookSize2sInSection1 = section1.count(bookSize2)

  #the number of swaps possible is the minimum of the two numbers directly above
  numPossibleSwaps = min(numBookSize1sInSection2, numBookSize2sInSection1)

  #swap books for section 1
  swappedBooks = 0 #stores the number of books swapped
  for i in range(len(section1)): #loop through the entire length of the section
    if swappedBooks == numPossibleSwaps: #if the number of swapped books has reached the limit we can swap, exit the loop
      break
    #if the current book is a book of size 2, then we replace it with a book that belongs in this section
    if section1[i] == bookSize2:
      section1[i] = bookSize1
      swappedBooks += 1 #increment swapped books by 1

  #swap books for section 2
  swappedBooks = 0 #stores the number of books swapped
  for i in range(len(section2)): #loop through the entire length of the section
    if swappedBooks == numPossibleSwaps: #if the number of swapped books has reached the limit we can swap, exit the loop
      break
    #if the current book is a book of size 1, then we replace it with a book that belongs in this section
    if section2[i] == bookSize1:
      section2[i] = bookSize2
      swappedBooks += 1 #increment swapped books by 1
  
  #return the number of swaps that were performed
  return numPossibleSwaps


#---MAIN---
bookOrder = input() #get the initial order of the books as a string
bookOrderList = [] #stores the order of the books as a list
#copy the string of books into a list
for book in bookOrder:
  bookOrderList.append(book)

#count the number of Large, Medium and Small books
numLs = bookOrderList.count('L')
numMs = bookOrderList.count('M')
numSs = bookOrderList.count('S')

#create three lists. One for the large books section, one for the medium books section and one for the small books section
sectionL = bookOrderList[:numLs]
sectionM = bookOrderList[numLs:numLs+numMs]
sectionS = bookOrderList[numLs+numMs:]

totalSwapCounter = 0 #stores the number of swaps we have performed so far

#swap the books that can be completed in one swap.
totalSwapCounter += swap('L', 'S') #swap the books from the large section and the small section
totalSwapCounter += swap('L', 'M') #swap the books from the large section and the medium section
totalSwapCounter += swap('M', 'S') #swap the books from the medium section and the small section

#now add the "leftovers". The books that require more than one move to be in the right section. Basiclly, the books that are still not in the right section / 3 * 2 
totalSwapCounter += int((sectionL.count('M') + sectionL.count('S') + sectionM.count('L') + sectionM.count('S') + sectionS.count('L') + sectionS.count('M')) / 3 * 2)

#print the total number of swaps needed to get the books in order
print(totalSwapCounter)
