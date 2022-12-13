from GRAPH import graph_load
from GRAPH import City_name


nodes, graph = graph_load('roadmap.dot', City_name.from_dict)

print(nodes["york"])

print(graph)

for neighbor in graph.neighbors(nodes["york"]):
    print(neighbor.name)

for neighbor, node_weights in graph[nodes["york"]].items():
    print(node_weights["distance"],neighbor.name)