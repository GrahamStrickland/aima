#!/usr/bin/env python3
"""Unit tests for BiBF-Search algorithm."""

from src.algorithms import bibf_search 
from src.data_structures import Problem


def test_uniform_cost_search(problem: Problem) -> None:
    solution = bibf_search(
        problem_b=problem, 
        ff=lambda node: node.path_cost,
        problem_f=problem, 
        fb=lambda node: node.path_cost,
    )

    assert solution.state == "Bucharest"
    assert solution.parent.state == "Fagaras"
    assert solution.parent.parent.state == "Sibiu"
    assert solution.parent.parent.parent.state == "Arad"
    assert solution.path_cost == 450
