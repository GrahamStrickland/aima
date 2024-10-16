#!/usr/bin/env python3
"""Depth-Limited-Search algorithm."""

from queue import LifoQueue

from .expand import expand
from ..data_structures import Node, Problem


def depth(node: Node) -> int:
    """Returns the depth of the given node in a tree-like search.

    Args:
        node (Node): A node generated by a tree-like search.

    Returns:
        depth (int): The depth of the node in the tree.
    """
    depth = 0

    while node.parent is not None:
        depth += 1
        node = node.parent

    return depth


def is_cycle(node: Node) -> bool:
    """Returns whether or not the path to the given node contains
    a cycle.

    Args:
        node (Node): A node generated by a tree-like search.

    Returns:
        is_cycle (bool): True if the path to the given node contains
                         a cycle, else false.
    """
    ancestor = node.parent

    while ancestor is not None:
        if ancestor.state == node.state:
            return True
        else:
            ancestor = ancestor.parent

    return False


def depth_limited_search(problem: Problem, l: int) -> Node | str | None:
    """Expands the root node, the next child, repeating this process
    until the depth limit is reached, then backtracking to the next
    successor of the root. This process is repeated until a goal is
    found or failure occurs.

    Args:
        problem: A problem instance.
        l: Depth limit for the search.

    Returns:
        A solution node or failure (None).
    """
    frontier: LifoQueue[Node] = LifoQueue()
    frontier.put(Node(state=problem.initial(), path_cost=0))
    result = None

    while not frontier.empty():
        node = frontier.get()

        if problem.is_goal(node.state):
            return node

        if depth(node) > l:
            result = "cutoff"
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.put(child)

    return result
