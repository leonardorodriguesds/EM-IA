from dataclasses import dataclass
import networkx as nx
import matplotlib.pyplot as plt
from .node import Node
from .edge import Edge

@dataclass
class Graph:
    """ Definição para um grafo simples """
    nodes: []
    edges: []

    def append_node(self, node):
        self.nodes.append(node)
        return (len(self.nodes) - 1)

    def append_edge(self, edge):
        self.edges.append(edge)

    def print(self):
        G = nx.Graph()
        G.add_nodes_from([(i, {'attr': x.attribute}) for i, x in enumerate(self.nodes)])
        G.add_edges_from([(x.node_from, x.node_to, {'attr': x.attribute}) for x in self.edges])
        pos = nx.spring_layout(G)
        nx.draw(G, pos)
        nx.draw_networkx_labels(G, pos, labels = nx.get_node_attributes(G, 'attr'), node_size=2000, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, labels = nx.get_edge_attributes(G, 'attr'))
        plt.savefig("depute_graph.png")
        plt.show()
