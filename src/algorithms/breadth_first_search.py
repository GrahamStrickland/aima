#!/usr/bin/env python3
"""Breadth-First-Search algorithm."""

from queue import Queue

from ..data_structures import Node, Problem
from .expand import expand


def breadth_first_search(problem: Problem) -> Node | None:
    """Expands the root node, then all successors, repeating this process
    until a goal is found or failure occurs.

    Args:
        problem: A problem instance.

    Returns:
        A solution node or failure (None).
    """
    node = Node(state=problem.initial(), path_cost=0)
    if problem.is_goal(node.state):
        return node

    frontier = Queue()
    frontier.put(node)
    reached: set[str] = set([problem.initial()])

    while not frontier.empty():
        node: Node = frontier.get()

        for child in expand(problem, node):
            s: str = child.state
            if problem.is_goal(s):
                return child

            if s not in reached:
                reached.add(child.state)
                frontier.put(child)

    return None
