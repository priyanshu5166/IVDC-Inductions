Below is the code for 3 path planning algorithm **[BFS, DIJKSTRAS, RRT]**

**[Breadth-First Search (BFS)]**

**Strengths:**

***Simplicity:*** BFS is easy to implement and conceptually straightforward.

***Shortest Path in Unweighted Graphs:*** BFS finds the shortest path in terms of the number of edges, making it ideal for unweighted grids or graphs.

***Guaranteed Solution:*** BFS will always find a solution if one exists in connected graphs.

***Level-wise Exploration:*** BFS explores nodes level by level, making it effective for scenarios that require exploring all nodes at a given distance from the source before moving deeper. 

**Weakness:**

***Inefficient for Weighted Graphs:*** BFS does not account for edge weights, so it cannot be used for optimal pathfinding in weighted graphs.

***Memory Usage:*** BFS stores many nodes in memory at once, especially for large graphs, making it inefficient for memory-constrained environments.

***Blind Search:*** BFS explores all nodes evenly, which can lead to exploring irrelevant nodes far from the goal.


**Applicability:**

***Pathfinding in Robotics:*** BFS helps in pathfinding for robots navigating through environments, ensuring that the robot explores all possible paths at a given distance before proceeding further

***Maze Solving:*** BFS is effective for solving mazes or grid-based environments where the objective is to find the shortest path from the start to the exit. It systematically explores all paths at the current depth before moving deeper, making it suitable for such applications



**[Dijkstra’s algorithm]**

**Strengths:**

***Optimality:*** Dijkstra’s algorithm guarantees the shortest path from the starting node to all other nodes in the graph.

***Explores All Shortest Paths:*** Unlike breadth-first search (BFS), Dijkstra’s algorithm explores the most promising path first, avoiding unnecessary exploration of longer paths.

***Efficient with Sparse Graphs:*** When paired with a priority queue, Dijkstra’s algorithm is efficient for graphs with relatively few edges.

**Weakness:**

***Lack of Heuristic Guidance:*** Dijkstra’s algorithm does not use heuristics like the one used in A*, to guide the search process, which can result in longer search times. 

***Inability to Handle Negative Edge Weights:*** Dijkstra’s algorithm cannot accommodate graphs with negative edge weights. If such weights are present, the algorithm may produce incorrect results.

***Inefficient for Dense Graphs:*** The time complexity can become prohibitive when dealing with dense graphs,

**Applicability:**

***Best suited for:*** Weighted graphs with non-negative edge weights, such as road networks, navigation systems, and any graph where optimal cost paths are needed.



**[Rapid-exploring Random Tree (RRT)]**

Rapidly-exploring Random Trees (RRT) is a sampling-based motion planning algorithm designed to efficiently explore large spaces.

**Strengths:**

***Efficiency in High Dimensions:*** RRTs are particularly effective in high-dimensional spaces, making them suitable for complex path planning where traditional methods may struggle.

***Rapid Exploration:*** Quickly explores the configuration space, even in environments with obstacles and provides good coverage of the search space.

***Optimization:*** RRT has various optimal versions, so can be easily optimized to get the most optimal path like that in RRT*.

**Weakness:**

***Computational and Memory Cost:*** The computational time increases with the complexity of the environment also Can be memory-intensive as the tree grows.

***Optimal Path Generation:*** The original RRT algorithm does not guarantee finding the optimal path, which can be a significant drawback in applications where path cost critical.

***Sampling Bias:*** RRTs rely on random sampling, which can lead to inefficient exploration in certain environments, particularly if the sampling is not well-distributed.

***Limited Performance in Narrow Passages:*** RRTs can struggle with narrow passages or tight spaces, where the random sampling may not adequately explore feasible paths. 

**Applicability:**

***Autonomous Vehicles:*** Path planning for autonomous driving where the environment is complex and dynamic.

***Robotics:*** RRTs facilitate path planning in environments with static and dynamic obstacles.

***Unmanned Aerial Vehicles:*** They are used for planning flight paths in dynamic and uncertain environments.




