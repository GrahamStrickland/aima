#!/usr/bin/env python3
"""Recursive-Best-First-Search algorithm."""

from sys import maxsize
from typing import Callable

from ..algorithms import expand
from ..data_structures import Node, Problem


def recursive_best_first_search(
    problem: Problem, h: Callable[[int], int]
) -> Node | None:
    """Attempts to mimic the operation of standard best-first search, but using
    only linear space.
    """
    solution, _ = rbfs(
        problem=problem,
        node=Node(state=problem.initial, path_cost=0),
        f_limit=maxsize,
        h=h,
    )

    return solution


def rbfs(
    problem: Problem, node: Node, f_limit: int, h: Callable[[int], int]
) -> tuple[Node, int]:
    """Keep trace of the f-value of the best alternative path available from
    any ancestor of the current node. If the current node exceeds this limit,
    unwind back to the alternative path until the best path is found.

    Args:
        problem: A problem instance.
        node:    A problem Node.
        f_limit: A variable to keep track of the f-value of the best alternative
                 path.

    Returns:
        A solution node or failure (None) and a new f-cost limit.
    """
    if problem.is_goal(node.state):
        return node

    successors = [s for s in expand(problem, node)]
    if len(successors) == 0:
        return None, maxsize

    for s in successors:  # update f with value from previous search
        s.f = max(s.path_cost + h(s), node.f)

    while True:
        best = min(s.f for s in successors)
        if best.f > f_limit:
            return None, best.f
        alternative = min(s.f for s in set(successors) - set(best))
        result, best.f = rbfs(problem, best, min(f_limit, alternative))
        if result is not None:
            return result, best.f
