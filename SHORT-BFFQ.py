import networkx as nx
from GRAPH import City_name, graph_load

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)

city1=nodes["aberdeen"]
city2=nodes["perth"]

for any, path in enumerate(nx.all_shortest_paths(graph,city1,city2),1):
    print(f"{any}.","->".join(city.name for city in path))
