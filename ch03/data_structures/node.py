#!/usr/bin/env python3
"""Node class for search problems."""

from dataclasses import dataclass


@dataclass
class Node:
    """A data structure to keep track of the search tree in a search problem.

    Attributes:
    state: A dict representing the state to which the node corresponds
    parent: The node in the tree that generated this node.
    action: A string representing the action that was applied to the parent's
            state to generate this node.
    path_cost: A float representing the total cost of the path from the initial
               state to this node.
    """

    state: dict
    parent: Node
    action: str
    path_cost: float
