#!/usr/bin/env python3
"""Best-First-Search algorithm."""

from typing import Callable

from ..data_structures import Node, PriorityQueue, Problem
from .expand import expand


def best_first_search(problem: Problem, f: Callable) -> Node | None:
    """On each iteration choose a node on the frontier with minimum f(n) value,
    return it if its state is a goal state, and otherwise apply expand() to
    generate child nodes.

    Args:
        problem: A problem instance.
        f: A cost function to be used in evaluating the next node to be expanded.

    Returns:
        A solution node or failure (None).
    """
    node = Node(state=problem.initial(), path_cost=0)
    frontier = PriorityQueue(f)
    frontier.add(node)
    reached: dict[str, Node] = {problem.initial(): node}

    while not frontier.is_empty():
        node: Node = frontier.pop()
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s: str = child.state
            if s not in reached.keys():
                reached[s] = child
                frontier.add(child)

    return None
