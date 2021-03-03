/*
Author: Ri Hong
Date AC'd: August 2, 2020
Problem: https://dmoj.ca/problem/ccc03s4
*/

//Explanation
/*
First we construct a suffix array. Then, for each string within the suffix array, we compute the length of the longest common prefix (LCP) between our string and the previous string in the suffix array. 
We then take the length of our current string and subtract the LCP we just calculated and add this value to a total/counter variable. We can then loop through all strings in the suffix array and perform
the same operation. After the last string is processed, we will then have the total number of distinct substrings stored in our total/counter variable. We have to remember to add 1 to the total to take into
account the suffix of an empty string.

I am not completely sure of how this algoritm works, but to my shallow understanding, the length of each suffix somehow represents how many substrings can be formed and the reason we subtract the lcp of the 
current suffix and the previous suffix is to remove duplicates.


For more info on Suffix Arrays: https://youtu.be/zqKlL3ZpTqs
For more info on LCP Arrays: https://youtu.be/53VIWj8ksyI
How to solve this problem using Suffix and LCP Arrays: https://www.geeksforgeeks.org/count-distinct-substrings-string-using-suffix-array/
*/

//Code
//Include libaries
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

//This function creates a suffix array (vector in this case) given a string. It returns back the pointer to the vector
vector<string>* createSuffixArray(string targetString){
  //create a vector to store suffixes
  vector<string>* suffixArray_ptr = new vector<string>;

  //fill vector with suffixes
  for(int i = 0; i < targetString.length(); i++){
    suffixArray_ptr->push_back(targetString.substr(i, targetString.length() - i));
  }

  //sort the suffixes lexicographically
  sort(suffixArray_ptr->begin(), suffixArray_ptr->end());

  //return the sorted vector
  return suffixArray_ptr;
}

//This function calculates the length of the longest common prefix between two given strings 
int lcp(string previousElement, string currElement){
  int lcpLength = 0; //stores the length of the lcp
  int shorterLength = previousElement.length() > currElement.length() ? currElement.length() : previousElement.length(); //shorthand for if(previousElement.length > currElement.length()) then return currElement.length() else: return previousElement.length()

  //find length of the lcp
  for(int i = 0; i < shorterLength; i++){
    if(previousElement[i] == currElement[i]){
      lcpLength++;
    }
    else{
      break;
    }
  }
  return lcpLength;
}

int findDistinctSubstrings(vector<string> suffixArray){
  int count = 0; //stores # of distinct substrings
  //iterate through the array and compare it with the previous element using lcp(longest common prefix)
  for(int i = 1; i < suffixArray.size(); i++){
    count += suffixArray[i].length() - lcp(suffixArray[i-1], suffixArray[i]);
  }
  //add occurance of the first substring and the occurance of the empty substring
  count += suffixArray[0].length() + 1;
  return count;
}

int main() {
  //Get input
  int nTestCases;
  string currentStr;
  cin >> nTestCases;

  for(int i = 0; i < nTestCases; i++){
    cin >> currentStr;
    //create a sorted array of suffixes
    vector<string>* pSuffixArray = createSuffixArray(currentStr);

    //find number of distinct substrings
    cout << findDistinctSubstrings(*pSuffixArray) << endl;

    //delete pointer to save memory
    delete pSuffixArray;
  }


}