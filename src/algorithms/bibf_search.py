#!/usr/bin/env python3
"""BiBf-Search algorithm."""

from typing import Callable

from .expand import expand
from ..data_structures import Node, PriorityQueue, Problem


def terminated(
    solution: Node | None, frontier_f: PriorityQueue, frontier_b: PriorityQueue
) -> bool:
    """Test to prove that there is no possible better soution remaining."""
    return True


def join_nodes(dir: str, node1: Node, node2: Node) -> Node:
    return node1


def proceed(
    dir: str, problem: Problem, frontier: PriorityQueue, reached: dict[str, Node],
    reached2: dict[str, Node], solution: Node | None) -> Node | None:
    """Expand node on frontier; check against the other frontier in reached2.
    
    Args: 
        dir: The direction: either 'F' for forward or 'B' for backward.
    """
    node = frontier.pop()

    for child in expand(problem=problem, node=node):
        s = child.state
        if s not in reached or child.path_cost < reached[s].path_cost:
            reached[s] = child
            frontier.add(child)

            if s in reached2:
                solution2: Node = join_nodes(dir, child, reached2[s])
                if solution2.path_cost < solution.path_cost:
                    solution = solution2

    return solution


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
    node_f = Node(state=problem_f.initial(), path_cost=0)
    node_b = Node(state=problem_b.initial(), path_cost=0)

    frontier_f = PriorityQueue(f=ff)
    frontier_f.add(node_f)
    frontier_b = PriorityQueue(f=fb)
    frontier_b.add(node_b)

    reached_f: dict[str, Node] = dict()
    reached_f[node_f.state] = node_f
    reached_b: dict[str, Node] = dict()
    reached_b[node_b.state] = node_b

    solution: Node | None = None

    while not terminated(
        solution=solution, frontier_f=frontier_f, frontier_b=frontier_b
    ):
        if ff(frontier_f.top()) < fb(frontier_b.top()):
            solution = proceed(
                dir="F", 
                problem=problem_f, 
                frontier=frontier_f, 
                reached=reached_f, 
                reached2=reached_b, 
                solution=solution
            )
        else:
            solution = proceed(
                dir="B", 
                problem=problem_b, 
                frontier=frontier_b, 
                reached=reached_b, 
                reached2=reached_f, 
                solution=solution
            )

    return solution
