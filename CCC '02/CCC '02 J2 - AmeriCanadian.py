'''
Author: Ri Hong
Date AC'd: Jan. 31, 2020
'''

#Explanation
'''
For each word, we need to check if it is spelt using the American spelling or the Canadian spelling. If it is spelt using the Canadian
spelling, we don't modify the word. If it is spelt using the American spelling, then we have to modify the word. We can tell if
a word is spelt using the American spelling or not because words that are spelt using the American spelling then it will:
1) End in "or"
2) Have a length greater than 4
3) Have a third last character that is a consonant

We can change words spelt using the American spelling to the Canadian spelling by simply:
1) removing the last two characters ("or")
2) adding "our"

Print the word out at the end.
'''

#Code
vowelList = ["a", "e", "i", "o", "u", "y"] #stores the list of vowels
while True: #loop
  word = input() #get the word as a string
  if word == "quit!": #if the word is "quit!"
      break #exit the loop

  #if the word is spelt using the American spelling
  if word.endswith("or") and len(word) > 4 and word[-3] not in vowelList: #if the word ends with "or", the length of the word is longer than 4 and the third last character is a consonant
    word = word[0: len(word)-2] + "our" #change the word to the canadian spelling. Take the word and replace the "or" with "our"

  #print the word
  print(word)

