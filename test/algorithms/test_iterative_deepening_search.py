#!/usr/bin/env python3
"""Unit tests for Iterative-Deepening-Search algorithm."""

from src.algorithms import iterative_deepening_search
from src.data_structures import Problem


def test_iterative_deepening_search(problem: Problem) -> None:
    solution = iterative_deepening_search(problem)

    assert solution.state == "Bucharest"
    assert solution.parent.state == "Fagaras"
    assert solution.parent.parent.state == "Sibiu"
    assert solution.parent.parent.parent.state == "Arad"
    assert solution.path_cost == 450
