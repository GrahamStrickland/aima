#!/usr/bin/env python3
"""Unit tests for Best-First-Search algorithm."""

from src.algorithms import expand, best_first_search 
from src.data_structures import Node, Problem


class TestBestFirstSearch:
    def test_expand(self, problem: Problem) -> None:
        for node in expand(problem, Node("Arad", parent=None, action=None, path_cost=0)):
            assert isinstance(node, Node)
            assert node.path_cost != 0
            assert node.action == "To" + node.state

            if node.parent == "Arad":
                assert node.state in {"Sibitu", "Timisoara", "Zerind"}

    def test_best_first_search(self, problem: Problem) -> None:
        solution = best_first_search(problem, lambda node: node.path_cost)

        assert solution.state == "Bucharest"
        assert solution.path_cost == 450
        assert solution.parent.state == "Pitesti"
        assert solution.parent.parent.state == "RimnicuVilcea"
        assert solution.parent.parent.parent.state == "Sibiu"
        assert solution.parent.parent.parent.parent.state == "Arad"
