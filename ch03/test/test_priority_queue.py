#!/usr/bin/env python3
"""Tests for PriorityQueue class."""

from typing import Callable

from ..data_structures import Node, PriorityQueue


def f(node: Node) -> float:
    return Node.path_cost


def test_init() -> None:
    a = Node(state={}, parent=None, action="none", path_cost=0.) 

    queue = PriorityQueue(f)

    assert queue is not None


def test_is_empty() -> None:
    a = Node(state={}, parent=None, action="move_to_b", path_cost=0.) 
    b = Node(state={}, parent=a, action="none", path_cost=2.) 

    queue = PriorityQueue(f)
    assert queue.is_empty()

    queue.add(a)
    assert not queue.is_empty()

    queue.add(b)
    assert not queue.is_empty()

    a = queue.pop()
    assert not queue.is_empty()

    a = queue.pop()
    assert queue.is_empty()

