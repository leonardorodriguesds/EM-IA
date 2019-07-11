import pandas as pd
from src import Node, Graph, Receipt, Edge

df_politicians = pd.read_csv('data/deputies_dataset.csv', low_memory=False)

# Lista de atributos importantes para a análise dos recibos
attributes = ['receipt_date', 'establishment_name', 'receipt_value']

_nodes_ = dict([(x, dict()) for x in attributes])
receipts, graphs, nodes_dict = [], dict(), dict()        
limit = 2                                                  # Limite de recibos
for _, row in df_politicians.iterrows():
    attrs = {}
    receipt = Node('receipt')                               # Cria um novo nó para o recibo
    attrs.update(row.items())                               # Salva este atributo do deputado
    print (attrs)

    deputy_id = attrs['deputy_id']

    # Recupera o grafo do deputado, ou cria um novo com seus atributos principais
    graph = graphs[deputy_id] if deputy_id in graphs else Graph(
        **{'nodes': [
            Node('deputy'), 
            Node(deputy_id), 
            Node(attrs['political_party']), 
            Node(attrs['state_code'])
        ], 'edges': [
            Edge(node_from=0, node_to=1, attribute='deputy_id'), 
            Edge(node_from=0, node_to=2, attribute='political_party'), 
            Edge(node_from=0, node_to=2, attribute='political_party'),
            Edge(node_from=0, node_to=3, attribute='state_code')
        ]})
    nodes = nodes_dict[deputy_id] if deputy_id in nodes_dict else _nodes_    
    id = graph.append_node(receipt)                         # Insere o recibo no grafo
    graph.append_edge(Edge(node_from=id, node_to=0, attribute='receipt'))
    for column, value in attrs.items():
        if attributes.count(column):
            """ Verifica se esse atributo é de interesse do algoritmo. """
            if value not in nodes[column]:
                """ 
                    Caso este atributo não possua um nó no grafo, então um novo é criado.
                    No grupo de controle nodes, é insirido nesta coluna uma tupla: {value, id}
                        * value Valor do atributo
                        * id ID do nó deste atributo e valor no grafo
                """
                attr_value_id = graph.append_node(Node(value))
                nodes[column].update({value: attr_value_id}) 
            else:
                """ Caso este atributo e valor já possua um nó no grafo, é recuperado seu ID. """
                attr_value_id = nodes[column][value]
            """ 
                Salva a relação deste atributo e valor para o atual deputado.
                Uma nova aresta é criada com as informações:
                    * node_from Nó do deputado
                    * node_to Nó do atributo valor
                    * attribute Label do atributo, ou coluna da tabela
            """
            graph.append_edge(Edge(node_from=id, node_to=attr_value_id, attribute=column))
    
    receipts.append(Receipt(**attrs))                         # Salva o deputado em uma lista de deputados
    graphs[deputy_id] = graph                               # Salva o grafo deste deputado
    nodes_dict[deputy_id] = nodes                           # Salva a relação de attr:id
    
    limit -= 1
    if limit == 0:
        break

print (len(graphs))

# Plota o primeiro deputado
list(graphs.values())[0].print()