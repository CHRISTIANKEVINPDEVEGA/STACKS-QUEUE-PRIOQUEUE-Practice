import networkx as nx
from GRAPH import City_name, graph_load,depth_first_traverse, depth_first_search as dfs

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("@", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
    else:
        print("Not found")

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = graph_load("roadmap.dot", City_name.from_dict)
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)


for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)