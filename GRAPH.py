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

