from dataclasses import dataclass
from .node import Node

@dataclass
class Edge:
    node_from: Node                     # Nó de origem
    node_to: Node                       # Nó de destino
    attribute: str                      # Label, ou atributo da aresta