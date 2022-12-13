from GRAPH import graph_load
from GRAPH import City_name


nodes, graph = graph_load('roadmap.dot', City_name.from_dict)

print(nodes["london"])

print(graph)