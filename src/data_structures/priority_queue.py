#!/usr/bin/env python3
"""Overloaded child class of PriorityQueue using evaluation function."""

from collections import deque
from typing import Callable

from .node import Node


class PriorityQueue(): 
    """First pops the node with the minimum cost according to some 
    evaluation function."""
    _frontier: deque[Node]

    def __init__(self, f: Callable[[Node], float]) -> None:
        """Initialises a priority queue ordered by f

        Args:
            f (Callable): Evaluation function for comparing nodes.
        """
        self._eval_func = f
        self._frontier = deque()

    def is_empty(self) -> bool:
        """Returns True only if there are no nodes in the frontier."""
        return len(self._frontier) == 0

    def pop(self) -> Node | None:
        """Removes the top node from the frontier and returns it.

        Returns:
            Node | None: top node from the frontier if the queue 
                is not empty, else None.
        """
        if not self.is_empty():
            return self._frontier.popleft()
        else:
            return None

    def top(self) -> Node | None:
        """Returns (but does not remove) the top node of the frontier.
        
        Returns:
            Node | None: top node from the frontier if the queue 
                is not empty, else None.
        """
        if not self.is_empty():
            return self._frontier[0]
        else:
            return None

    def add(self, node: Node) -> None:
        """Inserts node into its proper place in the queue.

        Args:
            node (Node): Node to be put into the queue.
        """
        self._frontier.append(node)

        while self._frontier[0].path_cost > node.path_cost:
            self._frontier.rotate(1)

