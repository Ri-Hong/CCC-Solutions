'''
Author: Ri Hong
Date AC'd: Feb 3, 2021
Problem: https://dmoj.ca/problem/ccc11s4
'''

#Explanation
"""
We make the observation that certain patients can accept less types of blood than others. Thus,
we priortize the patients that can accept the least types of blood first. 
Here is a list of which patients can accept which blood types, ascending:
Patient Type : Acceptable Blood Types
O- : O-
O+ : O+, O-
A- : A-, O-
A+ : A+, A-, O+, O-
B- : B-, O-
B+ : B+, B-, O+, O-
AB- : AB-, B-, A-, O-
AB+ : AB+, AB-, B+, B-, A+, A-, O+, O-

First, we create a list for the leftover blood by subtracting each type of blood by each type of patient.
If the value becomes less than 0, then we set it to 0, since that means that there is no excess blood for that blood type
Then we create a "patients uncured" list, by subtracting the number of each patient type by the corresponding
blood we have available. If the value becomes less than 0, then we set it to 0, since that means that al patients of 
that blood type are cured.
Now that we have a list of leftover blood and a list of uncured patients, we can start distributing the leftover
blood to the uncured patients, starting from the patients that can accept the least number of blood types.
We update the patients uncured and leftover blod list as we go. At the end, to find out the number of
cured patients, we take the sum of all the patients in the beginning and subtract the sum of all the
uncured patients from it.
"""

#Code
#Get input
bloodAval = list(map(int, input().split())) #get the # of units of each blood type and store them in bloodAval as integers
patientTypes = list(map(int, input().split())) #get the # of each type of patient, and store them in patientTypes as integers

bloodLeftover = [] #This list will store the leftover blood
patientsUncured = [] #This list will store the uncured patients
for i in range(8):
  bloodLeftover.append(bloodAval[i] - patientTypes[i]) #fill bloodLeftover by subtracting #blood - #patients of the same type
  patientsUncured.append(patientTypes[i] - bloodAval[i]) #fill patientsUncured by subtracting #patients - #blood of the same type

for i in range(8): #loop through bloodLeftover and patientsUncured. If any values are less than 0, set them to 0
  if bloodLeftover[i] < 0:
    bloodLeftover[i] = 0
  if patientsUncured[i] < 0:
    patientsUncured[i] = 0

#An index of each blood type. Used to avoid magic numbers further down
oNegLeftoverBlood = 0
oPosLeftoverBlood = 1
aNegLeftoverBlood = 2
aPosLeftoverBlood = 3
bNegLeftoverBlood = 4
bPosLeftoverBlood = 5
abNegLeftoverBlood = 6
abPosLeftoverBlood = 7

#An index of each patient type.
oNegPatientsUncured = 0
oPosPatientsUncured = 1
aNegPatientsUncured = 2
aPosPatientsUncured = 3
bNegPatientsUncured = 4
bPosPatientsUncured = 5
abNegPatientsUncured = 6
abPosPatientsUncured = 7

#This function takes the patient type and the blood type as an index. 
#It gives as many of the blood type passed in to as many of the patients of the patient type passed in
#ex. If you pass in oNegPatientsUncured(Index 0) and oNegLeftoverBlood(Index 0), it would give as much as 
#the O negative blood leftover to as many of the O negative patients
#Note that it updates the bloodLeftover and pateintsUncured lists as it performs the calculations

def calculate(pIndex, bIndex): #patientsUncured index, bloodLeftover index
  if patientsUncured[pIndex] < bloodLeftover[bIndex]: #if we have more blood than patients
    bloodLeftover[bIndex] -= patientsUncured[pIndex] #subtract the # of patients from the # of units of blood 
    patientsUncured[pIndex] = 0 #set the # of patients uncured 

  elif patientsUncured[pIndex] > bloodLeftover[bIndex]: #if we have more patients than blood
    patientsUncured[pIndex] -= bloodLeftover[bIndex] #subtract the # of units of blood from the # of patients 
    bloodLeftover[bIndex] = 0 #set the # of units of blood to 0 

  else: #same number of patients and blood
    patientsUncured[pIndex] = 0 #set # patients to 0
    bloodLeftover[bIndex] = 0 #set # of units of blood to 0

#distribute the excess blood
#carry for O pos
#---take from O neg
calculate(oPosPatientsUncured, oNegLeftoverBlood)

#carry for A neg
#---take from O neg
calculate(aNegPatientsUncured, oNegLeftoverBlood)

#carry for A pos
#---take from O pos
calculate(aPosPatientsUncured, oPosLeftoverBlood)
#---take from O neg
calculate(aPosPatientsUncured, oNegLeftoverBlood)
#---take from A neg
calculate(aPosPatientsUncured, aNegLeftoverBlood)

#carry for B neg
#---take from O neg
calculate(bNegPatientsUncured, oNegLeftoverBlood)

#carry for B pos
#---take from O pos
calculate(bPosPatientsUncured, oPosLeftoverBlood)
#---take from O neg
calculate(bPosPatientsUncured, oNegLeftoverBlood)
#--take from B neg
calculate(bPosPatientsUncured, bNegLeftoverBlood)

#carry for AB neg
#--take from O neg
calculate(abNegPatientsUncured, oNegLeftoverBlood)
#--take from A neg
calculate(abNegPatientsUncured, aNegLeftoverBlood)
#--take from B neg
calculate(abNegPatientsUncured, bNegLeftoverBlood)

#carry for AB pos
#--take from O neg
calculate(abPosPatientsUncured, oNegLeftoverBlood)
#--take from A neg
calculate(abPosPatientsUncured, aNegLeftoverBlood)
#--take from B neg
calculate(abPosPatientsUncured, bNegLeftoverBlood)
#--take from AB neg
calculate(abPosPatientsUncured, abNegLeftoverBlood)
#--take from O pos
calculate(abPosPatientsUncured, oPosLeftoverBlood)
#--take from A pos
calculate(abPosPatientsUncured, aPosLeftoverBlood)
#--take from B pos
calculate(abPosPatientsUncured, bPosLeftoverBlood)


numPatients = sum(patientTypes)
patientsCured = numPatients - sum(patientsUncured)
print(patientsCured)