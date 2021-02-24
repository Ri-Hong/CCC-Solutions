'''
Author: Ri Hong
Date AC'd: Feb. 24, 2021
'''

#Explanation
'''
To solve this problem, you have to do 2 things: 
1) Convert the improper fraction (in the case that it is improper) into a mixed number. E.g. 55/10 becomes 5 5/10
2) Reduce the fraction (Express it in the lowest terms) E.g. 55/10 becomes 11/2 (divided by 5)

You can choose to do those steps in any order.
To convert an improper fraction to a mixed number, we can use the floor division operator to divide the numberator
by the denominator. This will tell us how many times the denominator can go into the numerator. For example, 
with 55/10, the denominator (10) can go into the numerator (55) 5 times. So the whole number will be 5. Next we 
have to adjust the numerator accordingly (subtract the whole number multiplied by the denominator from the numerator).
E.g. Currently we have 5 55/10. It needs to be 5 5/10

To reduce a fraction, we first have to find both the numerator and the denominator's greatest common factor.
We can loop in reverse starting from the numerator and ending on the number 1. For each of those possible GCFs in between, 
check if both the numerator and denominator is divisible by the current GCF. Once the GCF is found, we can divide the denominators
and numerators accordingly to reduce the fraction.

Finally, we print the final result. Note that there are some edge cases that need to be handled. (When the whole number or the
numerator = 0)

'''

#Code
numerator = int(input()) #get the numerator as an integer
denominator = int(input()) #get the denominator as an integer

wholeNumber = numerator // denominator #calculate the whole number by seeing how many times the denominator goes into the numerator
numerator -= wholeNumber * denominator #adjust the numerator after we calculate the whole number

for GCF in range(numerator, 0, -1): #loop through the numbers from the numerator to 1. This number is the greatest common factor of the numberator and denominator
  if (denominator / GCF).is_integer() and (numerator / GCF).is_integer(): #if the numerator and denominator are both divisible by the GCF
    denominator = int(denominator / GCF) #divide the denominator by the GCF and int it to remove any decimal 0s
    numerator = int(numerator / GCF) #divide the numerator by the GCF and int it to remove any decimal 0s
    break #once a GCF is found, break. No need to keep looking for another GCF

#handle output
if wholeNumber == 0 and numerator == 0: #if both the whole number and the numerator are 0, print 0
  print(0)
elif wholeNumber == 0: #if only the whole number is 0, print only the numerator and denominator
  print("{}/{}".format(numerator, denominator))
elif numerator == 0: #if the numerator is 0, print only the whole number
  print(wholeNumber)
else: #If the numerator and whole number are not 0s, print the whole number, numerator and denominator
  print("{} {}/{}".format(wholeNumber, numerator, denominator))