import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from typing import List

DIRECTED = "DIRECTED"
UN_DIRECTED = "UN_DIRECTED"

def visualize(adjacency_matrix: List[List[int]], graph_type=DIRECTED):
    # 1. Create a graph object from the NumPy matrix
    # Use create_using=nx.Graph() for undirected graphs (matrix should be symmetric)
    # Use create_using=nx.DiGraph() for directed graphs
    if graph_type == DIRECTED:
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    if graph_type == UN_DIRECTED:
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.Graph)

    # 2. Draw the graph
    plt.figure(figsize=(6, 6)) # Optional: set the figure size
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_weight='bold', font_size=15)

    # 3. Display the plot
    plt.title("Graph Diagram from Adjacency Matrix")
    plt.show()

def visualize_v2(adjacency_matrix: List[List[int]], graph_type=DIRECTED):
    # 1. Create a graph object from the NumPy matrix
    # Use create_using=nx.Graph() for undirected graphs (matrix should be symmetric)
    # Use create_using=nx.DiGraph() for directed graphs
    if graph_type == DIRECTED:
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    if graph_type == UN_DIRECTED:
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.Graph)

    # 2. Define a layout for better visualization
    # Spring layout is a common choice
    pos = nx.spring_layout(G)
    # pos=nx.shell_layout(G)
    # pos=nx.planar_layout(G)
    # pos=nx.random_layout(G)

    # 3. Draw the graph
    # Use nx.draw_networkx for more control over labels and arrows
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='white')

    # Optional: Draw edge labels if your matrix entries represent weights
    # Here, we only have 0/1, so we can skip this, but the snippet is below for reference:
    # edge_labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # 4. Display the plot
    plt.title("Directed Graph from Adjacency Matrix")
    plt.axis('off') # Turn off the axis for a cleaner look
    plt.show()

if __name__ == '__main__':
    # Define the adjacency matrix (example for a simple undirected graph)
    # Matrix represents connections:
    # Node 0 is connected to 1 and 3
    # Node 1 is connected to 0 and 2
    # Node 2 is connected to 1 and 3
    # Node 3 is connected to 0 and 2
    sample_adjacency_matrix_1 = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ])

    sample_adjacency_matrix_2 = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0]
    ])

    visualize_v2(sample_adjacency_matrix_2, graph_type=DIRECTED)
