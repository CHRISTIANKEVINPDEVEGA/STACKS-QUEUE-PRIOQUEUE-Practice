import networkx as nx
from GRAPH import City_name, graph_load, breadth_first_traverse, breadth_first_search as bfs


def in_twentieth_century(year):
    return year and 1901 <= year <=2000

def arrangement(neighbors):
    def use_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=use_latitude, reverse=True))     

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)

for _node in nx.bfs_tree(graph, nodes["york"], sort_neighbors=arrangement):
    print("@", _node.name)
    if in_twentieth_century(_node.year):
        print("Found: ", _node.name, _node.year)
        break
    else:
        print("Not found")

print("\n\n\n")

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)
city = bfs(graph, nodes["york"], is_twentieth_century)
city.name


for city in breadth_first_traverse(graph, nodes["york"]):
    print(city.name)