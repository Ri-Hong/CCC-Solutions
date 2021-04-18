/*
Author: Ri Hong
Date AC'd: Jan 2, 2020
Problem: https://dmoj.ca/problem/ccc07j1
*/

%Explanation
/*
Keep switching the values of a, b, and c until they are in order, then print out b
*/
%Code
%Declare a, b, c and t (temporary)
var a, b, c, t : int
%Get input
get a,b,c

%Get a, b, and c in order
loop
    if a > b then
        t := b
        b := a
        a := t
    end if
    if b > c then
        t := c
        c := b
        b := t
    end if
    exit when
        a < b and b < c
end loop
%print b
put  b
