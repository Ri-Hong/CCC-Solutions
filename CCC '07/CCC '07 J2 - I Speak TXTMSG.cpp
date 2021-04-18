/*
Author: Ri Hong
Date AC'd: Apr 2, 2020
Problem: https://dmoj.ca/problem/ccc07j2
*/

//Explanation
/*
Get each textese message and translate it using if statements or a dictionary
*/

//Code
#include <iostream>
using namespace std;

int main() {
  string textese;
  //Keep getting the textese until TTYL shows up
  while (textese != "TTYL"){
    cin >> textese;
    //Translate the message
    if (textese == "CU") {
      cout << "see you \n";
    }
    else if (textese == ":-)") {
      cout << "I'm happy \n";
    }
    else if (textese == ":-(") {
      cout << "I'm unhappy \n";
    }
    else if (textese == ";-)") {
      cout << "wink \n";
    }
    else if (textese == ":-P") {
      cout << "stick out my tongue \n";
    }
    else if (textese == "(~.~)") {
      cout << "sleepy \n";
    }
    else if (textese == "TA") {
      cout << "totally awesome \n";
    }
    else if (textese == "CCC") {
      cout << "Canadian Computing Competition \n";
    }
    else if (textese == "CUZ") {
      cout << "because \n";
    }
    else if (textese == "TY") {
      cout << "thank-you \n";
    }
    else if (textese == "YW") {
      cout << "you're welcome \n";
    }
    else if (textese == "TTYL") {
      cout << "talk to you later \n";
    }
    else{
      cout << textese + "\n";
    }
  }
}