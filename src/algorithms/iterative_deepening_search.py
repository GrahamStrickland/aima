#!/usr/bin/env python3
"""Iterative-Deepening-Search algorithm."""

from sys import maxsize

from ..data_structures import Node, Problem
from .depth_limited_search import depth_limited_search


def iterative_deepening_search(problem: Problem) -> Node | None:
    """Expands the root node, the next child, repeating this process
    until with depth limit l in [0, 1, 2, ...,], then backtracking to
    the next successor of the root. This process is repeated until a
    goal is found or failure occurs.

    Args:
        problem: A problem instance.

    Returns:
        A solution node or failure (None).
    """
    for depth in range(0, maxsize):
        result = depth_limited_search(problem, depth)
        if not isinstance(result, str):
            return result
