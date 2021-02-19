'''
Author: Ri Hong
Date AC'd: Jan. 30, 2020
'''

#Explanation
'''
We will use a list to store the amount of water flowing through each stream, where the index represents the stream ID/number - 1 and the value representing
the amount of water that flows through tha particular stream. For example, [7, 1, 4]  means that stream 1's flow is 7, stream 2's is 1 and stream 3's is 4.
Keep in mind that the stream index is not equivalent to the stream number. The stream index is always - 1 of the stream number. For example, the flow of 
stream 2 can be accessed at index 1, and the flow of stream 39 can be accessed at index 38.

We put the values of the intial stream in the list. Then we can go through each of the commands/actions. There are three possible commands to process: 
split (99), join (88) and end (77). 

If the command is exit (77) we can stop processing commands. 

If the command is split (99), then we take two addition values: the number/ID of ther stream that is getting split and the percentage of water that flows to 
the left fork. Next, we take that percentage, divide it by 100 and multiply that with the amount of water in the initial stream to get the amount of water 
that flows left. For example, if the command tells us to split stream 4 and gives us a percentage of 55, then to get the amount of water in the left stream, 
we do streams[4-1] * 55/100. To get the amount of water that flows to the right stream, we can simply subtract the amount of water that flows to the left fork
from the total amount of water of the stream before it was split. So streams[4-1] - amount_of_water_that_flows_left. Then to update the streams list, we can 
replace the value at the index of the unsplit stream with the amount of water that flows left and create a new element with index + 1 that holds the value of
how much water flows to the right stream.

If the command is join (88), then we take one addition value: the number/ID of ther stream that is getting joined to the stream to the right. To join two streams, 
we simply take the amount of water in the left stream (at stream_index - 1) and we add it to the amount of water that's flowing in the right stream (at stream_index) 
to get the amount of water that will flow through the new, joined stream. We can take the index of the left stream and replace it's value with the the new joined stream value. 
Finally, we can remove the element at the index of the right stream.

At the end, just print out all the values in the streams list, as this will be the final form of the streams. Remember to round each value to the nearest integer.
'''
#Code
numStreams = int(input()) #get the number of initial streams as an integer
streams = [] #this will store the amount of water flowing through each stream
for i in range(numStreams): #loop through the number of initial streams
  streams.append(int(input())) #add the amount of water in each stream to the streams list

while True: #loop through each join/split event
  action = int(input()) #get the join/split/end command
  if action == 77: #if the action is 77, that means there are no more joins/splits after it, so we exit the loop
    break

  elif action == 99: #if the action is 99, that means there is a split
    streamID = int(input()) #get the number of the stream that is split (this is the index +1 of the stream we need to split)
    percentageFlow = int(input()) #get the percentage of water that flows to the left fork
    #note: the reason there is a streamID - 1 insead of just streamID is because the the stream number is one more than the list index at which it is stored. E.g. Stream 1 is stored at streams[0]
    amountLeftFork = percentageFlow/100 * streams[streamID - 1] #calculate the amount of water that flows to the left fork (%flow/100 * amount of water in initial stream)
    amountRightFork = streams[streamID - 1] - amountLeftFork #calculate the amount of water that flows to the right fork (amount of water in initial stream - amount of water flowing to the left fork)

    streams[streamID-1] = amountLeftFork #set the value at the current stream index to the amount of water that flows to the left fork
    streams.insert(streamID, amountRightFork) #insert the amount of water that flows to the right fork after the amount of water that flows to the left fork
    
  elif action == 88: #if the action is 88, that means there is a joining os 2 streams
    streamID = int(input()) #get the number of the stream that is split (this is the index +1 of the stream we need to split)
    streams[streamID-1] = streams[streamID-1] + streams[streamID] #add the values of the stream that is indexed at streamID - 1 (the left stream) and the stream that is indexed at streamID (the right stream) Replace the value at the index of the left stream with this value
    streams.pop(streamID) #remove the value at the index of the right stream

#print out all the streams in their final form. Remember to print each value rounded to the nearest integer
for i in range(len(streams)):
  print(round(streams[i]), end = " " )