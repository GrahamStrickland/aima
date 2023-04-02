#!/usr/bin/env python3
from random import randint

from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class RandomizedReflexAgent:
    def __init__(self):
        self._rules = {'Dirty': 'Suck',
                       'Clean': ['Left', 'Right', 'Up', 'Down']}

    def get_action(self, percept: Sensor) -> Actuator:
        state: dict[str, str] = self._interpret_input(percept)
        rule: Actuator = self._rule_match(state)
        action: str = rule.value

        return action

    @staticmethod
    def _interpret_input(percept: Sensor) -> dict:
        return {percept.name: percept.value}

    def _rule_match(self, state: dict[str, str]) -> Actuator:
        action: str = ''

        for k, v in state.items():
            if v == 'Dirty':
                action = self._rules[v]
            else:
                action = self._rules['Clean'][randint(0, len(self._rules['Clean']) - 1)]
            break

        return Actuator(name='action', value=action)