import networkx as nx
import matplotlib.pyplot as plt

def kruskal_mst(graph, display_steps=True):
    mst = nx.Graph()
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])
    
    disjoint_set = {node: {node} for node in graph.nodes()}
    
    for step, edge in enumerate(edges):
        node1, node2, weight = edge
        if disjoint_set[node1] != disjoint_set[node2]:
            mst.add_edge(node1, node2, weight=weight['weight'])
            set1 = disjoint_set[node1]
            set2 = disjoint_set[node2]
            set1.update(set2)
            for node in set2:
                disjoint_set[node] = set1
            if display_steps:
                print(f"Step {step + 1}: Added edge ({node1}-{node2}) with weight {weight['weight']}")
    
    return mst

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)

# Calcular el MST
mst = kruskal_mst(G, display_steps=True)

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
plt.title("Árbol de Expansión Mínima (MST) utilizando Kruskal")
plt.show()