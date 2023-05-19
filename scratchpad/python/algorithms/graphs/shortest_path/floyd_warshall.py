#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""
from typing import NamedTuple

from ..base import GraphAdjacencyMatrix, EdgeWithValue as Edge, EdgeId


class EdgeInfo(NamedTuple):
    weight: int
    intermediate_edge: EdgeId | None


def init_shortest_paths_graph(edge_weights_graph: GraphAdjacencyMatrix):
    shortest_paths_graph = GraphAdjacencyMatrix(
        vertices=edge_weights_graph.vertices,
        has_edge_values=True,
    )
    for edge in edge_weights_graph.edges:
        shortest_paths_graph.add_edge(
            Edge(
                edge.vertex_0, edge.vertex_1,
                EdgeInfo(weight=edge.value, intermediate_edge=None))
        )
    return shortest_paths_graph


def floyd_warshall_algorithm(edge_weights_graph: GraphAdjacencyMatrix):
    shortest_paths_graph = init_shortest_paths_graph(edge_weights_graph)


def main():
    pass


if __name__ == "__main__":
    main()
