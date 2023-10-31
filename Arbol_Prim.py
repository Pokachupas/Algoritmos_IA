import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph, display_steps=True):
    mst = nx.Graph()
    start_node = list(graph.nodes())[0]
    visited = {start_node}
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])

    while len(visited) < len(graph.nodes):
        possible_edges = [edge for edge in edges if edge[0] in visited and edge[1] not in visited]
        if not possible_edges:
            break
        best_edge = possible_edges[0]
        node1, node2, weight = best_edge
        mst.add_edge(node1, node2, weight=weight['weight'])
        visited.add(node2)
        if display_steps:
            print(f"Added edge ({node1}-{node2}) with weight {weight['weight']} to MST")

    return mst

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)

# Calcular el MST
mst = prim_mst(G, display_steps=True)

# Dibujar el grafo original
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo Original")
plt.show()

# Dibujar el MST
pos = nx.spring_layout(mst)
nx.draw(mst, pos, with_labels=True, node_size=700, node_color='lightgreen')
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
plt.title("Árbol de Expansión Mínima (MST) utilizando Prim")
plt.show()
