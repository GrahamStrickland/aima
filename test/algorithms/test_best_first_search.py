#!/usr/bin/env python3
"""Unit tests for Best-First-Search algorithm."""

from src.algorithms import expand, best_first_search 
from src.data_structures import Node, Problem, PriorityQueue


class TestBestFirstSearch:
    states = [
        Node(state="Arad", parent=None, action=None, path_cost=0),
        Node(state="Sibiu", parent="Arad", action="ToSibiu", path_cost=140),
        Node(state="Timisoara", parent="Arad", action="ToTimisoara", path_cost=118),
        Node(state="Zerind", parent="Arad", action="ToZerind", path_cost=75),
        Node(state="Oradea", parent="Sibiu", action="ToOradea", path_cost=151),
        Node(state="Fagaras", parent="Sibiu", action="ToFagaras", path_cost=99),
        Node(state="RimnicuVilcea", parent="Sibiu", action="ToRimniuVilcea", path_cost=80),
        Node(state="Lugoj", parent="Timisoara", action="ToLugoj", path_cost=111),
        Node(state="Oradea", parent="Zerind", action="ToOradea", path_cost=71),
        Node(state="Bucharest", parent="Fagaras", action="ToBucharest", path_cost=211),
        Node(state="Pitesti", parent="RimnicuVilcea", action="ToPitesti", path_cost=97),
        Node(state="Craiova", parent="RimnicuVilcea", action="ToCraiova", path_cost=146),
        Node(state="Mehadia", parent="Lugoj", action="ToMehadia", path_cost=70),
        Node(state="Urziceni", parent="Bucharest", action="ToUrziceni", path_cost=85),
        Node(state="Giurgiu", parent="Bucharest", action="ToGiurgiu", path_cost=90),
        Node(state="Pitesti", parent="Bucharest", action="ToPitesti", path_cost=101),
        Node(state="Bucharest", parent="Pitesti", action="ToBucharest", path_cost=101),
        Node(state="Craiova", parent="Pitesti", action="ToCraiova", path_cost=138),
        Node(state="Drobeta", parent="Mehadia", action="ToDrobeta", path_cost=75),
        Node(state="Vaslui", parent="Urziceni", action="ToVaslui", path_cost=142),
        Node(state="Hirsova", parent="Urziceni", action="ToHirsova", path_cost=98),
        Node(state="Craiova", parent="Drobeta", action="ToDrobeta", path_cost=120),
        Node(state="Iasi", parent="Vaslui", action="ToIasi", path_cost=92),
        Node(state="Eforie", parent="Hirsova", action="ToEforie", path_cost=86),
        Node(state="Neamt", parent="Vaslui", action="ToNeamt", path_cost=87)
    ]

    actions = {"ToSibiu", "ToTimisoara", "ToZerind", "ToOradea", "ToFagaras",
        "ToRimnicuVilcea", "ToLugoj", "ToBucharest", "ToPitesti", "ToCraiova",
        "ToMehadia", "ToUrziceni", "ToGiurgiu", "ToDrobeta", "ToVaslui", 
        "ToHirsova", "ToIasi", "ToEforie", "ToNeamt"
    }

    _problem = Problem(
        states=states, 
        initial_state="Arad", 
        goal_state="Bucharest",
        actions=actions,
        transition_model=lambda state, action: action[2:],
        action_cost=[lambda node: node.path_cost]
    )

    def test_expand(self) -> None:
        nodes = expand(self._problem, Node("Arad", parent=None, action=None, path_cost=0))

        assert nodes is not None

        for node in nodes:
            assert isinstance(node, Node)
            assert node.path_cost != 0
            assert node.action == "To" + node.state

            if node.parent() == "Arad":
                assert node.state in {"Sibiu", "Timisoara", "Zerind"}

    def test_best_first_search(self) -> None:
        pass
