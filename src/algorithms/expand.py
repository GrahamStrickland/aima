#!/usr/bin/env python3
"""Expand helper function for search algorithms."""

from typing import Generator

from ..data_structures import Node


def expand(problem, node: Node) -> Generator[Node, None, None]:
    """Expands a node and yields its children nodes.

    Args:
        problem: A problem instance.
        node: A node on the frontier in the search problem.

    Yields:
        A generator object containing the child nodes.
    """
    s = node.state

    for action in problem.actions(s):
        s_prime = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        yield Node(state=s_prime, parent=node, action=action, path_cost=cost)
