#!/usr/bin/env python3
"""Uniform-Cost-Search algorithm."""

from .best_first_search import best_first_search
from ..data_structures import Node, Problem


def uniform_cost_search(problem: Problem) -> Node | None:
    """Expands the root node, then choose the successor with least Path-Cost, 
    repeating this process until a goal is found or failure occurs.

    Args:
        problem: A problem instance.

    Returns:
        A solution node or failure (None).
    """
    return best_first_search(problem, lambda node: node.path_cost)
