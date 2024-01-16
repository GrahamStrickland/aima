#!/usr/bin/env python3
"""Unit tests for Problem data structure."""

from src.data_structures import Node, Problem


class TestProblem:
    _problem = Problem

    def test_constructor(self) -> None:
        states = [
            Node(state="Arad", parent=None, action=None, path_cost=0),
            Node(state="Sibiu", parent="Arad", action="ToSibiu", path_cost=140),
            Node(state="Timisoara", parent="Arad", action="ToTimisoara", path_cost=118),
            Node(state="Zerind", parent="Arad", action="ToZerind", path_cost=75),
            Node(state="Oradea", parent="Sibiu", action="ToOradea", path_cost=151),
            Node(state="Fagaras", parent="Sibiu", action="ToFagaras", path_cost=99),
            Node(state="RimnicuVilcea", parent="Sibiu", action="ToRimniuVilcea", path_cost=80),
            Node(state="Zerind", parent="Arad", action="ToZerind", path_cost=75)
        ]

        actions = set()

        transition_model = dict()

        self._problem = Problem(
            states=states, 
            initial_state="Arad", 
            goal_state="Bucharest",
            actions=actions,
            transition_model=transition_model,
            action_cost=[lambda node: node.path_cost]
        )

        assert isinstance(self._problem, Problem)

