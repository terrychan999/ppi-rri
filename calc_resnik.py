import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import fastobo


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

superclass_nodes = nx.descendants(knowledge_graph, "GO:0000001")
print(superclass_nodes)
superclass_nodes.add("GO:0000001")
super_graph = knowledge_graph.subgraph(superclass_nodes)
nx.draw(super_graph, pos=graphviz_layout(super_graph, prog="dot"), with_labels=True, arrows=True)
plt.show()
