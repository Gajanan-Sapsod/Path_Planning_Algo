# Path_Planning_Algo
## Table of Contents
* [Description](#Description "Goto Description")
* [Comparison](#Comparison "Goto Comparison")
* [Conclusion](#Conclusion "Goto Conclusion")
## Description
* Visualizations of the two most popular path planning algorithms, Dijkstra's and A*, are implemented in this repository using Pygame.

* Dijkstra's algorithm explores all possible paths from the starting point to the goal, while A* algorithm incorporates a distance heuristic.
## Comparison
|Dijkstra's Algorithm|Astar Algorithm|
|-----|--------|
|Dijkstra's algorithm explores all paths to reach the goal.| A* algorithm, on the other hand, tries to find a better path by using a heuristic function that gives priority to nodes expected to be more advantageous than others.
|In Dijkstra's algorithm, the next node is chosen based on the function f(v) = g(v), where g represents the cost accumulated so far.| In A* algorithm, the next node is chosen based on the function f(v) = g(v) + h(v), where g represents the cost accumulated so far and h is the heuristic function.
## Conclusion
### Dijkstra's algorithm
<img src="https://github.com/Gajanan-Sapsod/Path_Planning_Algo/assets/105559761/c811f395-2151-4d31-af43-1862eead7991" width="600" height="600" > 

### Astar algorithm
<img src="https://github.com/Gajanan-Sapsod/Path_Planning_Algo/assets/105559761/3067292c-9c62-4639-a7eb-9f60378f993e" width="600" height="600" >  
