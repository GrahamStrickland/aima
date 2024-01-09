#!/usr/bin/env python3
"""Tests for priority queue data structure."""

from src.data_structures import Node, PriorityQueue


def f(node: Node) -> float:
    return node.path_cost

def test_init() -> None:
    """Test for __init__() function"""
    queue = PriorityQueue(f)

    assert queue.is_empty()

