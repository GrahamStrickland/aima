#!/usr/bin/env python3
"""Unit tests for Recursive-Best-First-Search algorithm."""

from functools import partial
from sys import maxsize

from src.algorithms import recursive_best_first_search
from src.data_structures import Node, Problem


def hsld(node: Node, sld: dict[str, int]):
    if node.state in sld:
        return sld[node.state]
    return maxsize


class TestRecursiveBestFirstSearch:
    def test_recursive_best_first_search(
        self, problem: Problem, sld: dict[str, int]
    ) -> None:
        solution = recursive_best_first_search(problem, partial(hsld, sld=sld))

        assert solution.state == "Bucharest"
        assert solution.path_cost == 450
        assert solution.parent.state == "Fagaras"
        assert solution.parent.parent.state == "Sibiu"
        assert solution.parent.parent.parent.state == "Arad"
