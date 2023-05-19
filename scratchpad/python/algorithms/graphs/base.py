#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

from collections import defaultdict
from typing import NamedTuple, Hashable, Iterable

Vertex = Hashable
Vertices = Iterable[Vertex]
EdgeValue = any


class EdgeId(NamedTuple):
    vertex_0: Vertex
    vertex_1: Vertex


class EdgeWithValue(NamedTuple):
    vertex_0: Vertex
    vertex_1: Vertex
    value: EdgeValue


EdgeNoValue = EdgeId
Edge = EdgeNoValue | EdgeWithValue
EdgesNoValues = Iterable[EdgeNoValue]
EdgesWithValues = Iterable[EdgeWithValue]
Edges = EdgesNoValues | EdgesWithValues


class GraphAdjacencyMatrix:
    _edge_matrix: dict[EdgeId, any] = None
    _is_directed: bool = None
    _has_edge_values: bool = None
    _default_no_edge_value: any = None
    _default_edge_value: any = None
    _vertices: set = None

    def __init__(
            self, vertices: Vertices,
            is_directed: bool = False, has_edge_values: bool = False,
            default_no_edge_value: any = None, default_edge_value: any = True,
    ):
        self._is_directed = is_directed
        self._has_edge_values = has_edge_values
        self._default_edge_value = default_edge_value
        self._default_no_edge_value = default_no_edge_value
        self._vertices = set(vertices)
        self._edge_matrix = defaultdict(self._default_no_edge_value)

    def _init_edge_matrix(self, edges: Edges):
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge):
        edge_value = (edge.value
                      if self._has_edge_values
                      else self._default_edge_value)
        # try:
        #     edge_value = edge.value
        # except AttributeError:
        #     edge_value = self._default_edge_value
        edge_id = EdgeId(edge.vertex_0, edge.vertex_1)
        self._add_directed_edge(edge_id, edge_value)
        if not self._is_directed:
            edge_id = EdgeId(edge.vertex_1, edge.vertex_0)
            self._add_directed_edge(edge_id, edge_value)

    def _add_directed_edge(self, edge_id: EdgeId, value: any):
        self._edge_matrix[edge_id] = value

    def get_edge_value(self, edge_id: EdgeId) -> any:
        return self._edge_matrix[edge_id]

    def has_edge(self, edge_id: EdgeId) -> bool:
        return self.get_edge_value(edge_id) is not None

    def remove_edge(self, edge_id: EdgeId):
        self._edge_matrix.pop(edge_id)

    @property
    def vertices(self):
        return self._vertices

    def add_vertex(self, vertex: Vertex):
        self._vertices.add(vertex)

    @property
    def edges(self) -> Edges:
        return (self._edges_with_values()
                if self._has_edge_values
                else self._edges_no_values())

    def _edges_with_values(self) -> EdgesWithValues:
        return (
            EdgeWithValue(edge_id.vertex_0, edge_id.vertex_1, edge_value)
            for edge_id, edge_value
            in self._edge_matrix.items()
        )

    def _edges_no_values(self) -> EdgesNoValues:
        return (
            EdgeNoValue(edge_id.vertex_0, edge_id.vertex_1)
            for edge_id
            in self._edge_matrix.keys()
        )


def main():
    pass


if __name__ == "__main__":
    main()
