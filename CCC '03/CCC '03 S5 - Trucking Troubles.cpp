/*
Author: Ri Hong
Date AC'd: August 16, 2020
Problem: https://dmoj.ca/problem/ccc03s5
*/

//Explanation
/*
We have to construct a Minimum Spanning Tree (MST) that contains all the destination cities. When we are constructing the Tree, we can keep track of the smallest weight of the branches and that weight at the end is the largest
weight that can be driven through the destination cities. We build the tree one branch at a time until all destination cities are in the tree.
There are several MST algorithms like Prim's or Kruskal's. I chose Prim's but Kruskal's should work too. Feel free to research about MST algorithms if you are unsure about them.
*/

#include <bits/stdc++.h> //include all libraries
using namespace std;

int numCities, numRoads, numDestCities; //input variables

array<vector<pair<int, int>>, 100001> graph; //stores the cities. structure: [from: (weight, to)]
vector<int> destCities; //stores the cities we need to visit
array<bool, 10001> visited; //stores the cities that are already in the MST

int prims(){
  priority_queue<pair<int, int>, vector<pair<int, int>>> pq; //stores the roads in decreasing order. Roads that can support higher weights are at the top

  int smallestPossibleWeight = 100000; //stores the largest weight that can be driven through all cities (the road that can support the smallest weight)
  //start at city 1
  int currNode = 1; //initialize the current node to 1
  visited[1] = true; //set node 1 to visited

  int count = 0; //stores how many cities are already in the MST
  while(count != destCities.size()){ //keep looping until all the destination cities are in the MST
    //Keep in mind that pq.top() returns the road that can support the heaviest weight of all roads in the pq
    //pq.top().first is the weight that the current road can support
    //pq.top().second is the city that the current road connects to

    visited[currNode] = true; //set the current node to visited

    //add all connecting roads from the current node to the priority queue
    for(pair<int, int> i : graph[currNode]){
      pq.push(i);
    }
    //keep removing visited nodes until the top node is not visited
    while(visited[pq.top().second]){
      pq.pop();
    }
    //if the connecting city is a destination city
    if(find(destCities.begin(), destCities.end(), pq.top().second) != destCities.end()){
      count++; //increment the number of cities in the MST by 1
    }

    currNode = pq.top().second; //set the new current node to the road that the current node connects to
    //check if the smallestPossibleWeight needs to be updated
    if(pq.top().first < smallestPossibleWeight){
      smallestPossibleWeight = pq.top().first;
    }
    pq.pop(); //remove the current node we just procesed from the pq
  }
  return smallestPossibleWeight;
}



int main() {
  scanf("%d%d%d", &numCities, &numRoads, &numDestCities); //get input

  //add each road into the graph array
  for(int i = 0; i < numRoads; i++){
    int from, to, weight;
    scanf("%d%d%d", &from, &to, &weight);
    graph[from].push_back({weight, to});
    graph[to].push_back({weight, from});
  }

  //add each destination into the destCity array
  for(int i = 0; i < numDestCities; i++){
    int destCity;
    scanf("%d", &destCity);
    destCities.push_back(destCity);
  }
  cout << prims() << "\n"; //run the prims algorithm
}
