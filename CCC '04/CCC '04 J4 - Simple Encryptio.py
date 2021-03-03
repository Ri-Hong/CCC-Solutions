'''
Author: Ri Hong
Date AC'd: Feb 2, 2020
Problem: https://dmoj.ca/problem/ccc04j4
'''

#Explanation
'''
First we can create a shiftValue list used to store the shift value of each character of the keyword. For example, if the keyword was "ACT", the 
shiftValue list would be: [0, 2, 19], since 'A' means shift by 0, 'c' means shift by 2, and 'T' means shift by 19.

Now we have to loop through the message we want to encode and remove all non-alphanumeric characters from it.
Then we have to loop through every character of the message.
First, we have to determine which character of the keyword our current character corresponds to. This can be done using the modulus function.
Next, we have to shift the character.
    First, we get the numeric value of the character using the ord function.
    Then, we add the appropriate shift valve from the shiftValue list.
    Next, we have to deal with overflows, For example, if you shift 'Z' by 2, you would get 'B'. 
        So we have to subtract 65 from the value (since the ord('A') = 65 and we want 'A' = 0, 'B' = 1 etc.)
        Then, mod it by 26 (# chars in alphabet) to deal with numbers greater than 26
        Next, add 65 back onto the value since we subtracted 65 from before.
Finally, print out the encoded character
'''

#Code
#get the keyword and message as input()
keyword = input()
message = input()

shiftValue = [] #store the number of characters to shift by for each character of the keyword
#fill the shiftValue list
for i in range(len(keyword)):
  shiftValue.append(ord(keyword[i])-65)

#remove all non-alphanumeric characters from the string
messageAlpha = [] #stores the new string without non-alphanumeric characters
#loop through the message and copy all alphanumeric characters into messageAlpha
for i in range(len(message)):
  if message[i].isalpha():
    messageAlpha.append(message[i])


for i in range(len(messageAlpha)): #loop through the index of each character of the messageAlpha
  #skip the processing for spaces
  if messageAlpha[i] == " ":
    continue
  shiftIndex =  i % len(keyword) #find out which character of the keyword our current character corresponds with
  encodedCharacter = 65 + (ord(messageAlpha[i])-65 + shiftValue[shiftIndex]) % 26 #calculate the shift
  print(chr(encodedCharacter), end = "") #print out the encoded character
