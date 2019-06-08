import pandas as pd
from scripts import Node, Graph, Depute, Edge

df_politicians = pd.read_csv('data/deputies_dataset.csv', low_memory=False)

attributes = ['receipt_date', 'political_party', 'state_code', 'establishment_name', 'receipt_value']
graph = Graph([], [])
nodes = dict([(x, dict()) for x in attributes])
deputes = []
limit = 30
for _, row in df_politicians.iterrows():
    attrs = {}
    id = graph.append_node(Node('depute'))              # Insere um novo deputado no grafo
    for column, value in row.iteritems():
        """ Itera por todas as linhas da tabela. """
        attrs.update({ column: value })                 # Salva este atributo do deputado
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
    
    deputes.append(Depute(node_id=id, **attrs))             # Salva o deputado em uma lista de deputados

    """ Cria uma aresta do deputado para armazenar seu ID, para consultas suas informações futuramente. """
    attr_depute_id = graph.append_node(Node(len(deputes) - 1))
    graph.append_edge(Edge(node_from=id, node_to=attr_depute_id, attribute='depute_id'))
    limit -= 1
    if limit == 0:
        break

graph.print()