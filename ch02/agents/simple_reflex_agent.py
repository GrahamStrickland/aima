#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class SimpleReflexAgent:
    def __init__(self):
        self.rules = {'Dirty': 'Suck',
                      'A': 'Right',
                      'B': 'Left'}

    @staticmethod
    def _interpret_input(percept: Sensor) -> Environment:
        state = {percept.name: percept.value}

        return Environment('Square', state)

    def _rule_match(self, state: Environment) -> Actuator:
        if state.state == 'Dirty':
            action = self.rules[state.state]
        else:
            action = self.rules[state.name]

        return Actuator(name='action', value=action)

    def get_action(self, percept: Sensor) -> Actuator:
        state: Environment = self._interpret_input(percept)
        rule: Actuator = self._rule_match(state)
        action: str = rule.value

        return action
