#!/usr/bin/env python3
"""Unit tests for priority queue data structure."""

from src.data_structures import Node, PriorityQueue


def f(node: Node) -> float:
    return node.path_cost


class TestPriorityQueue:
    """Test suite for PriorityQueue data structure."""

    _queue = PriorityQueue(f)

    def test_init(self) -> None:
        assert self._queue.is_empty()

    def test_is_empty(self) -> None:
        assert self._queue.is_empty()

        self._queue.add(Node(state={}, parent=None, action="None", path_cost=0))

        assert not self._queue.is_empty()

        self._queue.pop()

        assert self._queue.is_empty()

    def test_pop(self) -> None:
        A = Node(state={}, parent=None, action="None", path_cost=0)
        self._queue.add(A)

        assert self._queue.top() == A

        self._queue.pop()

        assert self._queue.is_empty()

    def test_top(self) -> None:
        assert self._queue.top() == None

        A = Node(state={}, parent=None, action="None", path_cost=0)
        self._queue.add(A)

        assert self._queue.top() == A

        B = Node(state={}, parent=None, action="None", path_cost=1)
        self._queue.add(B)

        assert self._queue.top() == A

    def test_add(self) -> None:
        while not self._queue.is_empty():
            node = self._queue.pop()

        A = Node(state={}, parent=None, action="None", path_cost=0)
        B = Node(state={}, parent=None, action="None", path_cost=1)
        C = Node(state={}, parent=None, action="None", path_cost=2)

        assert self._queue.top() == None

        self._queue.add(C)

        assert self._queue.top() == C

        self._queue.add(A)

        assert self._queue.top() == A

        self._queue.add(B)

        assert self._queue.top() == A
