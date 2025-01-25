#!/usr/bin/env python3
"""BiBf-Search algorithm."""

from enum import Enum
from typing import Callable

from ..data_structures import Node, PriorityQueue, Problem
from .expand import expand


class Direction(Enum):
    F = 1
    B = 2


def terminated(
    solution: Node | None, frontier_f: PriorityQueue, frontier_b: PriorityQueue
) -> bool:
    """Test to prove that there is no possible better solution remaining."""

    return (
        solution is not None
        and solution.state == "Bucharest"
        and solution == frontier_f.top()
        and solution == frontier_b.top()
    )


def join_nodes(dir: Direction, node_f: Node, node_b: Node) -> Node:
    if dir == Direction.F:
        while node_b.parent is not None:
            if node_b.state == node_f.state:
                node = Node(
                    state=node_b.parent.state,
                    path_cost=node_b.parent.path_cost,
                    parent=node_f,
                    action=("To" + node_b.parent.state),
                )
            else:
                node = Node(
                    state=node_b.state,
                    path_cost=node_b.path_cost,
                    parent=node_f,
                    action=("To" + node_b.state),
                )

            node_f = node
            node_b = node_b.parent

        return node_f
    else:
        while node_f.parent is not None:
            if node_b.state == node_f.state:
                node = Node(
                    state=node_f.parent.state,
                    path_cost=node_f.parent.path_cost,
                    parent=node_b,
                    action=("To" + node_f.parent.state),
                )
            else:
                node = Node(
                    state=node_f.state,
                    path_cost=node_f.path_cost,
                    parent=node_b,
                    action=("To" + node_f.state),
                )

            node_b = node
            node_f = node_f.parent

        return node_b


def proceed(
    dir: Direction,
    problem: Problem,
    frontier: PriorityQueue,
    reached: dict[str, Node],
    reached2: dict[str, Node],
    solution: Node | None,
) -> Node | None:
    """Expand node on frontier; check against the other frontier in reached2.

    Args:
        dir: The direction: either 'F' for forward or 'B' for backward.
    """
    node = frontier.pop()

    for child in expand(problem=problem, node=node):
        s = child.state
        if s not in reached or (
            child.path_cost < reached[s].path_cost and child.path_cost > 0
        ):
            reached[s] = child
            frontier.add(child)

            if s in reached2:
                solution2: Node = join_nodes(dir, child, reached2[s])
                if solution is None or (
                    solution2.path_cost < solution.path_cost and solution2.path_cost > 0
                ):
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
        if frontier_f.is_empty() or frontier_b.is_empty():
            return solution

        if ff(frontier_f.top()) < fb(frontier_b.top()):
            solution = proceed(
                dir=Direction.F,
                problem=problem_f,
                frontier=frontier_f,
                reached=reached_f,
                reached2=reached_b,
                solution=solution,
            )
        else:
            solution = proceed(
                dir=Direction.B,
                problem=problem_b,
                frontier=frontier_b,
                reached=reached_b,
                reached2=reached_f,
                solution=solution,
            )

    return solution
