#!/usr/bin/env python3
"""Definition of priority queue."""

from typing import Callable

from .node import Node
from .queue import Queue


class PriorityQueue(Queue):
    """First pops the node with the minimum cost according to some evaluation 
    function, f."""

    def __init__(self, f: Callable) -> None:
        pass

