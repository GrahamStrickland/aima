#!/usr/bin/env python3
"""Unit tests for Recursive-Best-First-Search algorithm."""

from src.algorithms import recursive_best_first_search
from src.data_structures import Problem


class TestRecursiveBestFirstSearch:
    def test_recursive_best_first_search(self, problem: Problem) -> None:
        solution = recursive_best_first_search(problem, lambda node: node.path_cost)

        assert solution.state == "Bucharest"
        assert solution.path_cost == 450
        assert solution.parent.state == "Fagaras"
        assert solution.parent.parent.state == "Sibiu"
        assert solution.parent.parent.parent.state == "Arad"
