#!/usr/bin/env python3
"""Overloaded child class of PriorityQueue using evaluation function."""

from collections import deque 
from typing import Deque

from node import Node


class PriorityQueue(): 
    """First pops the node with the minimum cost according to some 
    evaluation function."""
    _frontier: deque[Node]

    def __init__(self, f: Callable) -> None:
        """Initialises a priority queue ordered by f

        Args:
            f: Evaluation function for comparing nodes.
        """
        self._eval_func = f
        self._frontier = deque()

    def put(self, item: Node) -> None:
        """Put item into the queue.

        Args:
            item: Node to be put into the queue.
        """
        pass

