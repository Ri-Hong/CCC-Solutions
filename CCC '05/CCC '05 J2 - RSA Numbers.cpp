/*
Author: Ri Hong
Date AC'd: Apr 2, 2020
Problem: https://dmoj.ca/problem/ccc05j2
*/

//Explanation
/*
Loop through all the numbers from the lower bounds to the upper bounds and check the number of factors 
*/

//Code
#include <iostream>
using namespace std;

int main() {
  //Get the lower and upper bounds
  int lowerBounds;
  int upperBounds;
  cin >> lowerBounds;
  cin >> upperBounds;
  int counter = 0; //Stores the # of valid RSA numbers
  int factorCounter; //Stores the # of factors for our current number

  //Loop through the numbers from the lower bounds to the upper bounds
  for (int i = lowerBounds; i <= upperBounds; i++){
    factorCounter = 0;
    for (int j = 1; j <= i; j++){ //Loop through all the numbers from 1 to our current number and count the # of factors
      if (i % j == 0){
        factorCounter ++;
      }
    }
    if (factorCounter == 4){ //If the # of factors is 4, increment the counter by 1
      counter ++;
    }
  }

  cout << "The number of RSA numbers between "; 
  cout << lowerBounds ; 
  cout << " and "; 
  cout << upperBounds; 
  cout << " is "; 
  cout << counter;
}