/*
Author: Ri Hong
Date AC'd: Jan 4, 2020
Problem: https://dmoj.ca/problem/ccc12j3
*/

%Explanation
/*
The input we get can be labeled as a scaling factor. We can seperate icon into three lines. For each line, we can use a for
loop to loop through the number of lines we need to print of that specific line. In the for loop we print each character
by the amount specified by scalingFactor.
*/
%Code
var scalingFactor : int
get scalingFactor %Get input
%Line 1
for i : 1 .. scalingFactor
  put repeat ("*", scalingFactor), repeat ("x", scalingFactor), repeat ("*", scalingFactor)
end for
%Line 2
for i : 1 .. scalingFactor
  put repeat (" ", scalingFactor), repeat ("x", 2 * scalingFactor)
end for
%Line 3
for i : 1 .. scalingFactor
  put repeat ("*", scalingFactor), repeat (" ",  scalingFactor), repeat ("*",  scalingFactor)
end for
