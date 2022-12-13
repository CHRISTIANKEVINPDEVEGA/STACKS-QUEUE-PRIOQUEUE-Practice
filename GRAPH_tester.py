from GRAPH import graph_load
from GRAPH import City_name


nodes, graph = graph_load('roadmap.dot', City_name.from_dict)

print(nodes["york"])

print(graph)

for neighbor in graph.neighbors(nodes["york"]):
    print(neighbor.name)

for neighbor, node_weights in graph[nodes["york"]].items():
    print(node_weights["distance"],neighbor.name)

def sorting(neighbors, approach):
    return sorting(neighbors.items(), key=lambda item: approach(item[1]))

def distance_length(node_weights):
    return float(node_weights["distance"])

for neighbors, node_weights in sorting(graph[nodes["york"]],distance_length):
    print(f"{node_weights['distance']:>3} miles, {neighbors.name}")