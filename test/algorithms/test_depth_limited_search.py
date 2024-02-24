#!/usr/bin/env python3
"""Unit tests for Depth-Limited-Search algorithm."""

from src.algorithms import depth, depth_limited_search, is_cycle 
from src.data_structures import Node, Problem


class TestDepthLimitedSearch:
    def test_depth(self, nodes: list[Node]) -> None:
        assert depth(nodes[-1]) == 6
        assert depth(nodes[-2]) == 6
        assert depth(nodes[-3]) == 6
        assert depth(nodes[-4]) == 5
        assert depth(nodes[-5]) == 5

    def test_is_cycle(self, nodes: list[Node]) -> None:
        assert not is_cycle(nodes[-1])
        assert not is_cycle(nodes[-2])
        assert not is_cycle(nodes[-3])
        assert not is_cycle(nodes[-4])
        assert not is_cycle(nodes[-5])

    def test_depth_limited_search(self, problem: Problem) -> None:
        solution = depth_limited_search(problem, 9)

        assert solution.state == "Bucharest"
        assert solution.parent.state == "Fagaras"
        assert solution.parent.parent.state == "Sibiu"
        assert solution.parent.parent.parent.state == "Arad"
        assert solution.path_cost == 450
