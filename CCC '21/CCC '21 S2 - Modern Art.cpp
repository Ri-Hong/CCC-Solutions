/*
Author: Ri Hong
Date AC'd: Feb 17, 2021
Problem: https://dmoj.ca/problem/ccc21s2
*/

//Explanation
/*
Instead of storing all the 'cells' in a 5000000 by 5000000 2D array, We can just store how many times each row/column is painted using 2 x 5000000 boolean arrays.
True/1 will mean that the row/col has been painted and False/0 will mean that the row/col has NOT been painted. Using booleans to store the state of the row/column
works since painting a single row/col once is equivalent to painting it three times, 5 times, 7 times, etc.
Along the way, we also keep a running total of how many rows and columns are painted.

We can observe that a square will olny become golden if either: the row is painted and the column isn't OR the row is not painted and the column is. (If row and 
column are painted or row and column are both not painted, then the square will remain black) This is similar to the exclusive or operator. 

Thus, the formula for the number of gold squares is: rowsUnpainted * columnsPainted + rowsPainted * columnsUnpainted.
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
array<bool, 5000000> rowState = {0}; //stores the number of times each row has been painted
array<bool, 5000000> colState = {0}; //stores the number of times each column has been painted

int main() {
  //get input
  scanf("%d", &height);
  scanf("%d", &width);
  scanf("%d", &nChoices);

  //loop through all instructions and update the rowState and colState arrays
  for(int i = 0; i < nChoices; i++){
    scanf("%s", &instruction); //'R' or 'C'
    scanf("%d", &rcIndex); //the col/row number to be flipped
    rcIndex--; //make the index zero based

    if(instruction == 'R'){
      rowState[rcIndex] = !rowState[rcIndex]; //"flip" the row. If it is currently a 1, make it 0 and vice versa
      nRowTrues += rowState[rcIndex]*2 - 1; //if the new state is true/gold, then we add one to the counter, if it's false/black, we subtract one from the counter
    }
    else if(instruction == 'C'){
      colState[rcIndex] = !colState[rcIndex]; //"flip" the row. If it is currently a 1, make it 0 and vice versa
      nColTrues += colState[rcIndex]*2 - 1; //if the new state is true/gold, then we add one to the counter, if it's false/black, we subtract one from the counter
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