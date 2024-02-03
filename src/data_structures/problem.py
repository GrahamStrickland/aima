#!/usr/bin/env python3
"""Data structure for problems in search spaces."""

from typing import Callable

from .node import Node


class Problem:
    """Data structure to implement a model problem.

    Attributes:
        states (list[str]): A set of possible states that the environment 
            can be in.
        initial_state (str): The initial state that the agent starts in.
        goal_states (str): States defined by a property that applies to
            one or many states indicating that the problem solution has
            been found.
        actions (Callable): The actions available to the agent.
        transition_model (Callable): Describes what each action does.
        action_cost (Callable): Gives the numeric cost of applying action
            a in state s to reach state s'.
    """
    _states: list[str]
    _initial_state: str 
    _goal_state: str
    _actions: Callable[[str], str]
    _transition_model: Callable[[str], Node]
    _action_cost: Callable[[str], float]

    def __init__(
        self,
        states: list[Node],
        initial_state: Node,
        goal_state: Node,
        actions: Callable[[str], set[str]],
        transition_model: Callable[[str], Node],
        action_cost: Callable[[str], float]
    ):
        self._states = states
        self._initial_state = initial_state
        self._goal_state = goal_state
        self._actions = actions
        self._transition_model = transition_model
        self._action_cost = action_cost

    def initial(self) -> str:
        return self._initial_state

    def is_goal(self, state: str) -> bool:
        return state == self._goal_state 

    def actions(self, state: str) -> set[str]:
        return self._actions(state)

    def result(self, state: str, action: str) -> str:
        return self._transition_model(state, action)

    def action_cost(self, state: str, action: str, state_p: str) -> float:
        return self._action_cost(state, action, state_p)
