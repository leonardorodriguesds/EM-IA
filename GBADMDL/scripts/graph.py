from dataclasses import dataclass

@dataclass
class Graph:
    """ Definição para um grafo simples """
    nodes: []
    edges: [[]]

    def append_node(self, node):
        self.nodes.append(node)

    def create_edge(self, i, j):
        self.edges[i].append(j)
        self.edges[j].append(i)