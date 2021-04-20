/*
Author: Ri Hong
Date AC'd: Aug 17, 2020
Problem: https://dmoj.ca/problem/ccc15j1
*/

//Explanation
/*
To make comparisons easier, we can convert the month and day integers into a single floating point number. We can divide the 
day integer by 100 and add it the month integer. For example, 2 and 18 becomes 2.18 and 12 and 30 becomes 12.30. By doing this,
we can just compare the result to 2.18 (Feburary 18). If the calculated number is equal to 2.18, then the day is the special day.
If the number is greater than 2.18, then the day is after Feburary 18. If the number is less than 2.18, then the day is before 
Feburary 18
*/

//Code
#include <bits/stdc++.h>
using namespace std;

int main() {
    float month, day; //Declare month and day as floats since we will be doing division on them
    scanf("%f%f", &month, &day); //Get input
    double sum = month + day/100; //Perform the operation
    if(day == 18 && month == 2){ //For some reason, (sum == 2.18) doesn't work in cpp, so I compared day and month instead
        printf("Special");
    }
    else if(sum > 2.18){ //After
        printf("After");
    }
    else if(sum < 2.18){ //Before
        printf("Before");
    }
}