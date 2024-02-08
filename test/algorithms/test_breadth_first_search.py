#!/usr/bin/env python3
"""Unit tests for Breadth-First-Search algorithm."""

from src.algorithms import breadth_first_search 
from src.data_structures import Problem


def test_best_first_search(problem: Problem) -> None:
    solution = breadth_first_search(problem)

    assert solution.state == "Bucharest"
    assert solution.state.parent == "Fagaras"
    assert solution.state.parent.parent == "Sibiu"
    assert solution.state.parent.parent.parent == "Arad"
    assert solution.path_cost == 450
