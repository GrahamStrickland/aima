#!/usr/bin/env python3
"""Unit tests for Uniform-Cost-Search algorithm."""

from src.algorithms import uniform_cost_search
from src.data_structures import Problem


def test_uniform_cost_search(problem: Problem) -> None:
    solution = uniform_cost_search(problem)

    assert solution.state == "Bucharest"
    assert solution.parent.state == "Fagaras"
    assert solution.parent.parent.state == "Sibiu"
    assert solution.parent.parent.parent.state == "Arad"
    assert solution.path_cost == 450
