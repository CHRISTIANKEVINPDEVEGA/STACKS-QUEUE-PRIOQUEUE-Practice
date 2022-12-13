from typing import NamedTuple
import networkx as nx


class City_info(NamedTuple):
    name: str
    country: str
    year: int or None
    latitude: float
    longtitude: float

    @classmethod
    def from_dict(cls,attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["years"]) or None,
            latitude=float(attrs["latitude"]),
            longtitude=float(attrs["longtitude"]),

        )

def graph_load(filename,node_factory):
    graph = nx.nx_araph.read_dot(filename)
    nodes = {
        name:node_factory(attributes)
        for name,attributes in graph.nodes(data=True)
    }

    return nodes, nx.Graph(
        (nodes[name1],nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

