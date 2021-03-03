'''
Author: Ri Hong
Date AC'd: Mar 2, 2021
Problem: https://dmoj.ca/problem/ccc02j1
'''

#Explanation
'''
We can store all the possible line patterns in an array (Theres only 5). By line patterns, I am referring the number of ways the asterisk can be arranged on a line.
Then we can hardcode the specific order of line patterns needed to create each number.

For example, the digit 8 requires:
1 x 3 astericks in the center
3 x One asterisk on each side
1 x 3 astericks in the center
3 x One asterisk on each side
1 x 3 astericks in the center



Note that the output cannot contain any trailing whitespace.
For example, if I represent spaces with underscores, and I wanted to output the first line of the digit 8, it would look like: _*_*_*. _*_*_*_ would be marked as wrong. 
'''

#create all the possible patterns for each line
linePatterns = ["", "", "", "", ""]
linePatterns[0] = [" * * *"]
linePatterns[1] = ["*     *"]
linePatterns[2] = ["      *"]
linePatterns[3] = [""]
linePatterns[4] = ["*"]

#create all the possible numbers using patterns
numPattern = ["", "", "", "", "", "", "", "", "", ""]
numPattern[0] = [0, 1, 1, 1, 3, 1, 1, 1, 0]
numPattern[1] = [3, 2, 2, 2, 3, 2, 2, 2, 3]
numPattern[2] = [0, 2, 2, 2, 0, 4, 4, 4, 0]
numPattern[3] = [0, 2, 2, 2, 0, 2, 2, 2, 0]
numPattern[4] = [3, 1, 1, 1, 0, 2, 2, 2, 3]
numPattern[5] = [0, 4, 4, 4, 0, 2, 2, 2, 0]
numPattern[6] = [0, 4, 4, 4, 0, 1, 1, 1, 0]
numPattern[7] = [0, 2, 2, 2, 3, 2, 2, 2, 3]
numPattern[8] = [0, 1, 1, 1, 0, 1, 1, 1, 0]
numPattern[9] = [0, 1, 1, 1, 0, 2, 2, 2, 0]

number = int(input()) #get the number to be printed

#print the number
for i in numPattern[number]:
  print(linePatterns[i][0])
