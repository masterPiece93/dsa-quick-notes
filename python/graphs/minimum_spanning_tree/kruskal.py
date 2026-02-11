"""
Minimum Spanning Tree 
===================================

- a Minimum Spanning Tree (MST) does not depend on a source node .
- a Shortest Path Tree (SPT) does .
- An MST is a global property of a graph, representing the minimum possible total edge weight to connect all vertices .
- works of negetive weights also , but not for negetive weight cycle .
- While algorithmically you may start building an MST from a specific vertex (e.g., Prim's algorithm), 
the resulting set of edges and the total weight of the MST will be the same regardless of which node is chosen as the starting point .

### Visualize :
- algorithms-visual.com/kruskal/?nodes=20_62_A~113_20_B~95_151_C~200_119_D~159_243_E~281_189_F~372_195_G~379_22_H~466_113_I&edges=0_1_6~1_3_2~0_2_4~2_3_10~3_5_0~2_4_4~4_5_7~4_6_1~5_6_6~6_7_1~6_8_33~7_8_44~1_7_3&directed=0

"""

# ---

# Reresentation of graph ( with cycle ) that we'll use for demonstration
GRAPH_REPRESENTATION = """
                                                            Graph :
                                                                - Un-Directed
                                                                - Connected
                                                                - Weighted

                                                            +---+              3                +---+
                                                          / | 1 | -----------------------------| 6 |            
                                                         /  +---+ \                            +---+\
                                                        /          \                             |   \  44
                                                    6  /            \                            |    \
                                                      /              \ 2                     1   |     \ +---+
                                                     /                \                          |      \| 8 |
                                                    /                  \                         |      /+---+
                                              +---+/                  +---+                      |     /
                                              | 0 |                   | 3 |\                     |    / 33
                                              +---+\                 /+---+ \                    |   /
                                                    \               /      0 \ +---+     6     +---+/
                                                     \             /          \| 5 |-----------| 7 |
                                                    4 \           /  10        +---+           +---+
                                                       \         /               /             /
                                                        \  +---+/               /             /
                                                         \ | 2 |               /             /
                                                           +---+ \            /  7          /  1
                                                                  \          /             /
                                                                   \        /             /
                                                                 4  \      /             /
                                                                     \    /             /
                                                                      \ +---+__________/
                                                                       \| 4 | 
                                                                        +---+ 

                                                                Edge Explaination

                                                                        0 <--> 1
                                                                        0 <--> 2
                                                                        1 <--> 3
                                                                        2 <--> 3
                                                                        2 <--> 4                          
"""

# Resultant Minimum Spanning Tree
"""

```txt
                                                            +---+              3               +---+
                                                            | 1 | -----------------------------| 6 |            
                                                            +---+ \                            +---+ 
                                                                   \                             |      
                                                                    \                            |     
                                                                     \ 2                     1   |       +---+
                                                                      \                          |       | 8 |
                                                                       \                         |      /+---+
                                              +---+                   +---+                      |     /
                                              | 0 |                   | 3 |\                     |    / 33
                                              +---+\                  +---+ \                    |   /
                                                    \                      0 \ +---+           +---+/
                                                     \                        \| 5 |           | 7 |
                                                    4 \                        +---+           +---+
                                                       \                                       /
                                                        \  +---+                              /
                                                         \ | 2 |                             /
                                                           +---+ \                          /  1
                                                                  \                        /
                                                                   \                      /
                                                                 4  \                    /
                                                                     \                  /
                                                                      \ +---+__________/
                                                                       \| 4 | 
                                                                        +---+ 

```

> __minimum weight : 48__
"""

from typing import *

# Custom Types

# - a node ( vertex ) type
Node = NewType('Node', int)

# - a weight/cost/priority type
Weight = NewType('Weight', int)

# - a weight/cost of edge type
EdgeWeight = NewType('EdgeWeight', Weight)

# - a cost of path type
PathCost = NewType('PathCost', Weight)

# - a graph type
Graph = NewType('Graph', Dict[Node, Set[Tuple[Node, EdgeWeight]]]) # Weighted Adjacency List

# Graph ( in adjacency list repr )
graph_with_cycle: Graph = {
    0: { 1, 2 },
    1: { 0, 3 },
    2: { 0, 3, 4 },
    3: { 1, 2 },
    4: { 2 }
}

# ---
