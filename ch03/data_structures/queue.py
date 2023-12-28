#!/usr/bin/env python3
"""Data structure to store the frontier of a search problem."""

from .node import Node


class Queue:
    """Base class for all queue types."""
    __frontier: list[Node] = []

    def __init__(self) -> None:
        pass

    def is_empty(self) -> bool:
        """Returns true only if there are no nodes in the frontier."""
        return len(self.__frontier) == 0

    def pop(self) -> Node:
        """Removes the top node from the frontier and returns it."""
        self.__frontier.pop()

    def top(self) -> Node | None:
        """Returns but does not remove the top node of the frontier."""
        return self.__frontier[0] if not self.is_empty() else None

    def add(self, node: Node) -> None:
        """Inserts node into its proper place in the queue."""
        self.__frontier.append(node)

