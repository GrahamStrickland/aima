#!/usr/bin/env python3
"""Best-First-Search algorithm."""

from typing import Callable, Generator

from ..data_structures import Node, PriorityQueue, Problem


def expand(problem, node: Node) -> Generator[Node, None, None]:
    """Expands a node and yields its children nodes.

    Args:
        problem:
        node: A node on the frontier in the search problem.

    Yields:
        A generator object containing the child nodes.
    """
    s = node.state

    for action in problem.actions(s):
        s_prime = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        yield Node(state=s_prime, parent=node, action=action, path_cost=cost)


def best_first_search(problem: Problem, f: Callable) -> Node | None:
    """On each iteration choose a node on the frontier with minimum f(n) value,
    return it if its state is a goal state, and otherwise apply expand() to 
    generate child nodes.

    Args:
        problem:
        f: 

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
