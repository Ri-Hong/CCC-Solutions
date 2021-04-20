'''
Author: Ri Hong
Date AC'd: Aug 26, 2020
Problem: https://dmoj.ca/problem/ccc12j2
'''

#Explanation
'''
Get the 4 readings and if they are in acsending order, the fish is rising. If they are in descending order, the fish is diving.
If the readings are equal, then the fish is at a constant depth. If the readings are none of the above, then there is no fish.
'''
#Code
#Get readings
reading = int(input())
reading2 = int(input())
reading3 = int(input())
reading4 = int(input())
#Compare the readings
if reading < reading2 < reading3 < reading4:
  print("Fish Rising")
elif reading > reading2 > reading3 > reading4:
  print("Fish Diving")
elif reading == reading2 == reading3 == reading4:
  print("Fish At Constant Depth")
else:
  print("No Fish")