#!/usr/bin/env python3
"""Recursive-Best-First-Search algorithm."""

from sys import maxsize
from typing import Callable

from ..algorithms import expand
from ..data_structures import Node, Problem


def recursive_best_first_search(problem: Problem, h: Callable) -> Node | None:
    """Attempts to mimic the operation of standard best-first search, but using
    only linear space.
    """
    solution, _ = rbfs(
        problem=problem,
        node=Node(problem.initial(), parent=None, path_cost=0),
        f_limit=maxsize,
        h=h,
    )

    return solution


def rbfs(problem: Problem, node: Node, f_limit: int, h: Callable) -> tuple[Node, int]:
    """Keep trace of the f-value of the best alternative path available from any
    ancestor of the current node. If the current node exceeds this limit, unwind
    back to the alternative path until the best path is found.

    Args:
        problem: A problem instance.
        node:    A problem Node.
        f_limit: A variable to keep track of the f-value of the best alternative
                 path.

    Return:
        A solution node or failure (None) and a new f-cost limit.
    """
    if problem.is_goal(node.state):
        return node, f_limit

    successors = [s for s in expand(problem, node)]
    if len(successors) == 0:
        return None, maxsize

    for s in successors:  # update f with value from previous search
        s.f = (
            max(s.path_cost + h(s), node.f)
            if node.f is not None
            else s.path_cost + h(s)
        )

    while True:
        best = min(zip([s.f for s in successors], [s for s in successors]))[1]
        if best.f > f_limit:
            return None, best.f

        runners_up = []
        for s in successors:
            if s != best:
                runners_up.append(s)
        alternative = min(s.f for s in runners_up) if len(runners_up) > 0 else 0

        result, best.f = rbfs(problem, best, min(f_limit, alternative), h)
        if result is not None:
            return result, best.f
