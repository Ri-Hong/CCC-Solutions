/*
Author: Ri Hong
Date AC'd: June 2, 2020
Problem: https://dmoj.ca/problem/ccc20j4
*/

//Explanation
/*
We can use a for loop to loop through all the cyclic shifts of a text. Then for each iteration of the for loop/cyclic shift,
check if the shifted text is a substring of the larger string.
*/

//Code
#include <iostream>
#include <string>
using namespace std;

bool isCS = false;
string sentence; //Stores the string, T
string originalWord; //Stores the original, unshifted text/word, S
string word; //Stores a cyclic shifted version of the original word

int index = 1;

int main() {
  //Get input
  cin >> sentence;
  cin >> originalWord;

  //Assign word to be the orignal word initially
  word = originalWord;

  //Loop through each cyclic shift
  while (index < word.length()+1){
    if (sentence.find(word, 0) != string::npos) { //If the word is found in the sentence
      isCS = true;
      break;
    }
    else{ //If the word is not found in the sentence
        //Update the word for the next iteration of the loop by adding the next character to the end of it and removing the first character
        word = originalWord + originalWord.substr(0, index); 
        word.erase(0, index); 
      }
    index++;
  }

  //Check if the sentence contains a cyclic shift of the word
  if (isCS){
    cout << "yes";
  }else{
    cout << "no";
  }
}