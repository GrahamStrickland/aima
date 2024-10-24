#!/usr/bin/env python3
"""Unit tests for Breadth-First-Search algorithm."""

from src.algorithms import breadth_first_search
from src.data_structures import Problem


def test_breadth_first_search(problem: Problem) -> None:
    solution = breadth_first_search(problem)

    assert solution.state == "Bucharest"
    assert solution.parent.state == "Fagaras"
    assert solution.parent.parent.state == "Sibiu"
    assert solution.parent.parent.parent.state == "Arad"
    assert solution.path_cost == 450
