import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()
    unvisited = set(graph.keys())

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

        visited.add(current_node)
        yield visited.copy(), distances.copy()

def draw_graph(graph, pos, visited, distances):
    plt.figure(figsize=(10, 10))
    labels = {node: f"{node}\n({distances[node]})" for node in graph}
    node_colors = ['g' if node in visited else 'r' for node in graph]

    nx.draw(graph, pos, labels=labels, with_labels=True, node_color=node_colors)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Calcular distancias con el algoritmo de Dijkstra
start_node = 'A'
dijkstra_result = list(dijkstra(graph, start_node))

# Crear el gráfico
G = nx.Graph(graph)
pos = nx.spring_layout(G)

# Visualizar el proceso
for visited, distances in dijkstra_result:
    draw_graph(G, pos, visited, distances)