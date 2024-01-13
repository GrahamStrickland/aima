#!/usr/bin/env python3
"""Unit tests for priority queue data structure."""

from src.data_structures import Node, PriorityQueue

def f(node: Node) -> float:
    return node.path_cost


class PriorityQueueTest:
    """Test suite for PriorityQueue data structure."""
    _queue: PriorityQueue

    def __init__(self):
        self._queue = PriorityQueue(f)


    def test_init(self) -> None:
        assert self._queue.is_empty()

    def test_is_empty(self) -> None:
        assert self._queue.is_empty()

        self._queue.add(Node(state={}, parent=None, action="None", path_cost=0))

        assert not self._queue.is_empty()

        self._queue.pop()

        assert self._queue.is_empty()

