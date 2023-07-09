# Path_Planning_Algo
## Table of Contents
* [Description](#Description "Goto Description")
* [Comparison](#Comparison "Goto Comparison")
* [Conclusion](#Conclusion "Goto Conclusion")
## Description
Visualisation of two most popular path planning algorithms, Dijkstra and A* is done in this repository using pygame.
Given the goal and starting point, Dijkstra's algorithm explores all possible paths to reach to goal, whereas Astar algorithm sets the distance heuristic .
## Comaparison
|Dijkstra's Algorithm|Astar Algorithm|
|-----|--------|
|Dijkstra's algorithm explores all paths to reach to goal| Astar  tries to look for a better path by using a heuristic function which gives priority to nodes that are supposed to be better than others 
|Considering g is cost so far, Dijkstra's algo chooses next node according to f(v)=g(v)| Considering g is cost so far and h as heuristic , Astar choose next node according to f(v)=g(v)+h(v)|
## Conclusion
### Dijkstra's algorithm
<img src="https://github.com/Gajanan-Sapsod/Path_Planning_Algo/assets/105559761/3067292c-9c62-4639-a7eb-9f60378f993e" width="600" height="600" > 

### Astar algorithm
<img src="https://github.com/Gajanan-Sapsod/Path_Planning_Algo/assets/105559761/c811f395-2151-4d31-af43-1862eead7991" width="600" height="600" >  

