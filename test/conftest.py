#!/usr/bin/env python

from pytest import fixture

from src.data_structures import Node, Problem


@fixture
def nodes() -> list[Node]:
    nodes = [Node(state="Arad", parent=None, action=None, path_cost=0)]
    nodes += [
        Node(state="Sibiu", parent=nodes[0], action="ToSibiu", path_cost=140),
        Node(state="Timisoara", parent=nodes[0], action="ToTimisoara", path_cost=118),
        Node(state="Zerind", parent=nodes[0], action="ToZerind", path_cost=75),
    ]
    nodes += [
        Node(state="Oradea", parent=nodes[1], action="ToOradea", path_cost=151),
        Node(state="Fagaras", parent=nodes[1], action="ToFagaras", path_cost=99),
        Node(
            state="RimnicuVilcea",
            parent=nodes[1],
            action="ToRimnicuVilcea",
            path_cost=80,
        ),
        Node(state="Lugoj", parent=nodes[2], action="ToLugoj", path_cost=111),
        Node(state="Oradea", parent=nodes[3], action="ToOradea", path_cost=71),
    ]
    nodes += [
        Node(state="Bucharest", parent=nodes[5], action="ToBucharest", path_cost=211),
        Node(state="Pitesti", parent=nodes[6], action="ToPitesti", path_cost=97),
        Node(state="Craiova", parent=nodes[6], action="ToCraiova", path_cost=146),
        Node(state="Mehadia", parent=nodes[7], action="ToMehadia", path_cost=70),
    ]
    nodes += [
        Node(state="Urziceni", parent=nodes[9], action="ToUrziceni", path_cost=85),
        Node(state="Giurgiu", parent=nodes[9], action="ToGiurgiu", path_cost=90),
        Node(state="Pitesti", parent=nodes[9], action="ToPitesti", path_cost=101),
        Node(state="Craiova", parent=nodes[10], action="ToCraiova", path_cost=138),
        Node(state="Drobeta", parent=nodes[12], action="ToDrobeta", path_cost=75),
    ]
    nodes += [
        Node(state="Vaslui", parent=nodes[13], action="ToVaslui", path_cost=142),
        Node(state="Hirsova", parent=nodes[13], action="ToHirsova", path_cost=98),
        Node(state="Craiova", parent=nodes[17], action="ToDrobeta", path_cost=120),
    ]
    nodes += [
        Node(state="Iasi", parent=nodes[18], action="ToIasi", path_cost=92),
        Node(state="Eforie", parent=nodes[19], action="ToEforie", path_cost=86),
        Node(state="Neamt", parent=nodes[18], action="ToNeamt", path_cost=87),
    ]

    return nodes


@fixture
def problem(nodes) -> Problem:
    return Problem(
        states={node.state for node in nodes},
        initial_state="Arad",
        goal_state="Bucharest",
        actions=lambda state: {
            (
                node.action
                if node.parent is not None and node.parent.state == state
                else None
            )
            for node in nodes
        }
        - {None},
        transition_model=lambda _, action: action[2:],
        action_cost=lambda s, a, s_p: next(
            node.path_cost
            for node in nodes
            if node.state == s_p
            and node.parent is not None
            and node.parent.state == s
            and node.action == a
        ),
    )


@fixture
def problem_b(nodes) -> Problem:
    return Problem(
        states={node.state for node in nodes},
        initial_state="Bucharest",
        goal_state="Arad",
        actions=lambda state: {
            (
                node.action
                if node.parent is not None and node.parent.state == state
                else None
            )
            for node in nodes
        }
        - {None},
        transition_model=lambda _, action: action[2:],
        action_cost=lambda s, a, s_p: next(
            node.path_cost
            for node in nodes
            if node.state == s_p
            and node.parent is not None
            and node.parent.state == s
            and node.action == a
        ),
    )


@fixture
def sld() -> dict[str, int]:
    """Straight-line distances to Bucharest."""
    return {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Drobeta": 242,
        "Eforie": 161,
        "Fagaras": 176,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 100,
        "Rimnicu Vilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374,
    }
