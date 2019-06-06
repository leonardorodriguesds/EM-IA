import pandas as pd
from scripts import Node, Graph

df_politicians = pd.read_csv('data/deputies_dataset.csv', low_memory=False)
# df_dirty_politicians = pd.read_csv('data/dirty_deputies_v2.csv', low_memory=False)

graph = Graph([], [[]])
for _, row in df_politicians.iterrows():
    args = {}
    for column, value in row.iteritems():
        args.update({ column: value })
    graph.append_node(Node(**args))