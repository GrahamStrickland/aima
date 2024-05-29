#!/usr/bin/env python3
"""BiBf-Search algorithm."""

from typing import Callable

from ..data_structures import Node, Problem


def bibf_search(
        problem_f: Problem, ff: Callable, problem_b: Problem, fb: Callable
) -> Node | None:
    """Keeps two frontiers and two tables of reached states, joining the two 
    frontiers once the same state has been reached in both to yield a solution.

    Args:
        problem_f: A problem instance.
        ff: A cost function to be used in evaluating the next node to be expanded.
        problem_b: Another instance of the same problem as problem_f.
        fb: The same cost function as ff.

    Returns:
        A solution node or failure (None).
    """
    pass
