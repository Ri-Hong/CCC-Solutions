/*
Author: Ri Hong
Date AC'd: Feb 17, 2020
Problem: https://dmoj.ca/problem/ccc21s2
*/

//Explanation
/*
Instead of storing all the 'cells' in a 5000000 by 5000000 2D array, We can just store how many times each row/column is painted using 2 x 5000000 arrays.
Then we loop through those two arrays and mod each value by 2 since painting a single row/col once is equivalent to painting it three times, 5 times, 7 times, etc.

We can observe that a square will olny become golden if either: the row is painted and the column isn't OR the row is not painted and the column is. (If row and 
column are painted or row and column are both not painted, then the square will remain black) This is similar to the exclusive or operator. 

So we can go through the 2 arrays and count how many rows are painted and how many columns are painted. We can also get the number of unpainted rows/columns. 
Now to find the number of squares, we can do rowsUnpainted * columnsPainted + rowsPainted * columnsUnpainted.
*/

#include <iostream>
#include <array>
using namespace std;

int height, width, nChoices;
char instruction; //stores whether the "choice" is a 'R' or 'C'
int rcIndex; //stores the index corresponding to the choice
int numGoldSquares = 0; //stores the number of gold squares
int nRowTrues, nColTrues = 0; //stores how many rows and cols are painted 
int nRowFalses, nColFalses; //stores how many rows and cols are NOT painted 
array<int, 5000000> rowState = {0}; //stores the number of times each row has been painted
array<int, 5000000> colState = {0}; //stores the number of times each column has been painted

int main() {
  //get input
  scanf("%d", &height);
  scanf("%d", &width);
  scanf("%d", &nChoices);

  //loop through all instructions and update the rowState and colState arrays
  for(int i = 0; i < nChoices; i++){
    scanf("%s", &instruction);
    scanf("%d", &rcIndex);

    if(instruction == 'R'){
      rowState[rcIndex-1]++;
    }
    else if(instruction == 'C'){
      colState[rcIndex-1]++;
    }
  }

  //loop through the rowState and colState arrays and mod each value by 2 to turn it into a boolean array. Update nRowTrues and nColTrues along the way
  for(int i = 0; i < 5000000; i++){
    if(rowState[i] % 2 == 1){
      nRowTrues++;
    }
    if(colState[i] % 2 == 1){
      nColTrues++;
    }
  }
  //calculate nRowFalses and nRowTrues
  nRowFalses = height - nRowTrues;  
  nColFalses = width - nColTrues;

  //calculate number of gold squares
  numGoldSquares += nRowTrues * nColFalses;
  numGoldSquares += nColTrues * nRowFalses;

  //output
  printf("%d", numGoldSquares);
}