#!/usr/bin/env python3
"""Unit tests for Depth-Limited-Search algorithm."""

from src.algorithms import depth, depth_limited_search, is_cycle 
from src.data_structures import Node, Problem


class TestDepthLimitedSearch:
    def test_depth(node: Node) -> None:
        pass

    def test_is_cycle(node: Node) -> None:
        pass

    def test_depth_limited_search(problem: Problem) -> None:
        solution = depth_limited_search(problem)

        assert solution.state == "Bucharest"
        assert solution.parent.state == "Fagaras"
        assert solution.parent.parent.state == "Sibiu"
        assert solution.parent.parent.parent.state == "Arad"
        assert solution.path_cost == 450
