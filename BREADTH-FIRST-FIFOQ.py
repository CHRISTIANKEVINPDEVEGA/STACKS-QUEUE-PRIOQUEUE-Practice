import networkx as nx
from GRAPH import City_name, graph_load

def in_twentieth_century(year):
    return year and 1901 <= year <=2000

def arrangement(neighbors):
    def use_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=use_latitude, reverse=True))     

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)

for _node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=arrangement):
    print("@", _node.name)
    if in_twentieth_century(_node.year):
        print("Found: ", _node.name, _node.year)
        break
    else:
        print("Not found")