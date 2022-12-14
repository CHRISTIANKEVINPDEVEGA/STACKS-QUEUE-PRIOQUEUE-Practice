import networkx as nx
from GRAPH import City_name, graph_load, shortest_path, connected

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)

city1=nodes["aberdeen"]
city2=nodes["perth"]

for any, path in enumerate(nx.all_shortest_paths(graph,city1,city2),1):
    print(f"{any}.","->".join(city.name for city in path))

print("\n\n\n")



print(" -> ".join(city.name for city in shortest_path(graph, city1, city2)))


def by_latitude(city):
    return -city.latitude

print(" -> ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))


print("\n\n\n")


print(connected(graph, nodes["belfast"], nodes["glasgow"]))

print(connected(graph, nodes["belfast"], nodes["derry"]))
