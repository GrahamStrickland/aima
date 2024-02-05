#!/usr/bin/env python

from pytest import fixture

from src.data_structures import Node, Problem


@fixture
def nodes() -> list[Node]:
    return [
        Node(state="Arad", parent=None, action=None, path_cost=0),
        Node(state="Sibiu", parent="Arad", action="ToSibiu", path_cost=140),
        Node(state="Timisoara", parent="Arad", action="ToTimisoara", path_cost=118),
        Node(state="Zerind", parent="Arad", action="ToZerind", path_cost=75),
        Node(state="Oradea", parent="Sibiu", action="ToOradea", path_cost=151),
        Node(state="Fagaras", parent="Sibiu", action="ToFagaras", path_cost=99),
        Node(state="RimnicuVilcea", parent="Sibiu", action="ToRimnicuVilcea", path_cost=80),
        Node(state="Lugoj", parent="Timisoara", action="ToLugoj", path_cost=111),
        Node(state="Oradea", parent="Zerind", action="ToOradea", path_cost=71),
        Node(state="Bucharest", parent="Fagaras", action="ToBucharest", path_cost=211),
        Node(state="Pitesti", parent="RimnicuVilcea", action="ToPitesti", path_cost=97),
        Node(state="Craiova", parent="RimnicuVilcea", action="ToCraiova", path_cost=146),
        Node(state="Mehadia", parent="Lugoj", action="ToMehadia", path_cost=70),
        Node(state="Urziceni", parent="Bucharest", action="ToUrziceni", path_cost=85),
        Node(state="Giurgiu", parent="Bucharest", action="ToGiurgiu", path_cost=90),
        Node(state="Pitesti", parent="Bucharest", action="ToPitesti", path_cost=101),
        Node(state="Craiova", parent="Pitesti", action="ToCraiova", path_cost=138),
        Node(state="Drobeta", parent="Mehadia", action="ToDrobeta", path_cost=75),
        Node(state="Vaslui", parent="Urziceni", action="ToVaslui", path_cost=142),
        Node(state="Hirsova", parent="Urziceni", action="ToHirsova", path_cost=98),
        Node(state="Craiova", parent="Drobeta", action="ToDrobeta", path_cost=120),
        Node(state="Iasi", parent="Vaslui", action="ToIasi", path_cost=92),
        Node(state="Eforie", parent="Hirsova", action="ToEforie", path_cost=86),
        Node(state="Neamt", parent="Vaslui", action="ToNeamt", path_cost=87)
    ]
    

@fixture
def problem(nodes) -> Problem:
    return Problem(
        states={node.state for node in nodes}, 
        initial_state="Arad", 
        goal_state="Bucharest",
        actions=lambda state: {(node.action if node.parent == state else None) \
                for node in nodes} - {None}, 
        transition_model=lambda _, action: action[2:],
        action_cost=lambda s, a, s_p: next(node.path_cost for node in nodes if \
                node.state == s_p and node.parent == s and node.action == a)
    )
