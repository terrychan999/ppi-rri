import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import fastobo

import os
currentPath = os.getcwd()  # current directory path
databasesPath = os.path.join(currentPath, "databases")
TermTxtPath = os.path.join(databasesPath, "go_term_path.txt")


knowledge_graph = nx.DiGraph()

go = fastobo.load('databases/go.obo')
for frame in go:
    if isinstance(frame, fastobo.term.TermFrame):
        knowledge_graph.add_node(str(frame.id))
        for clause in frame:
            if isinstance(clause, fastobo.term.IsAClause):
                knowledge_graph.add_edge(str(frame.id), str(clause.term))
            # elif isinstance(clause, fastobo.term.RelationshipClause):
            #     if (clause.raw_value().rstrip(" "+str(clause.term)) == "part_of"):
            #         knowledge_graph.add_edge(str(frame.id), str(clause.term))

# print(nx.is_directed_acyclic_graph(knowledge_graph))

go_term_path = open(TermTxtPath, "w")
for node in sorted(knowledge_graph.nodes):
    superclass_nodes = nx.descendants(knowledge_graph, node)
    superclass_nodes.add(node)
    super_graph = knowledge_graph.subgraph(superclass_nodes)
    value = list(reversed(list(nx.algorithms.topological_sort(super_graph))))
    #value = list(reversed(list(nx.algorithms.lexicographical_topological_sort(super_graph))))
    if len(value) == 0:
        go_term_path.write(f"{node}\t{node}\n")
    else:
        go_term_path.write(f"{node}\t{','.join(value)}\n")
go_term_path.close()

# nx.draw(super_graph, pos=graphviz_layout(super_graph, prog="dot"), with_labels=True, arrows=True)
# plt.show()
