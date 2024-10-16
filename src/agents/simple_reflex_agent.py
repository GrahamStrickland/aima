#!/usr/bin/env python3
from ..data_structures import Actuator, Sensor


class SimpleReflexAgent:
    def __init__(self):
        self._rules = {"Dirty": "Suck", "Clean": {"A": "Right", "B": "Left"}}

    def get_action(self, percept: Sensor) -> Actuator:
        state: dict[str, str] = self._interpret_input(percept)
        rule: Actuator = self._rule_match(state)
        action: str = rule.value

        return action

    @staticmethod
    def _interpret_input(percept: Sensor) -> dict:
        return {percept.name: percept.value}

    def _rule_match(self, state: dict[str, str]) -> Actuator:
        action: str = ""

        for k, v in state.items():
            if v == "Dirty":
                action = self._rules[v]
            else:
                action = self._rules["Clean"][k]
            break

        return Actuator(name="action", value=action)
