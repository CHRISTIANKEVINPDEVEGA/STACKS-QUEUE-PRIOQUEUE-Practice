import networkx as nx
from GRAPH import City_name, graph_load, dijkstra_shortest_path

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)

city1 = nodes["london"]
city2 = nodes["edinburgh"]

def distance(weights):
    return float(weights["distance"])

for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)



def weight(node1, node2, weights):
    return distance(weights)

for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)
