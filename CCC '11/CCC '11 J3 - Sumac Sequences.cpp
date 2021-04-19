/*
Author: Ri Hong
Date AC'd: Dec 30, 2020
Problem: https://dmoj.ca/problem/ccc11j3
*/

//Explanation
/*
The numbers in the sequence can be stores in a list/array/vector. To get the next number in the sequence, just subtract the
number at index n from the number that is one index before it. Keep doing this until a number in the sequence becomes greater
than the previous number
*/

//Code
#include<iostream>
#include<vector>
using namespace std;

int num1, num2;
int difference;
int currentIndex = 1;
vector<int> sequence; //Stores the sequence

int main() {
    scanf("%d%d", &num1, &num2); //Get input
    //Add first 2 numbers to the array
    sequence.push_back(num1);
    sequence.push_back(num2);
    while(sequence[currentIndex] <= sequence[currentIndex-1]){ //While the current number is still greater than or equal to the previous number
        difference = sequence[currentIndex-1] - sequence[currentIndex]; //Calculate difference
        sequence.push_back(difference); //Add the next number to the sequence
        currentIndex++;
    }

    printf("%lu\n", sequence.size()); //Output
}