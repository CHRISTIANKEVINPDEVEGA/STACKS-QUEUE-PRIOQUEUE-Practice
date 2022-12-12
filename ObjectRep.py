import networkx as nx
print(nx.nx_agraph.read_dot("roadmap.dot"))

graphinfo = nx.nx_agraph.read_dot("roadmap.dot")
print(graphinfo.nodes["london"])