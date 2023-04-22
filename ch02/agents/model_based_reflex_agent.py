#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class ModelBasedReflexAgent:
    def __init__(self, environment: Environment, rules: dict, transition_model: dict):
        self._state = {'Environment': environment, 'Points': 0}
        self._transition_model = transition_model 
        self._sensor_model = Sensor(None, None)
        self._rules = rules 
        self._action = Actuator('action', None)

    def get_action(self, percept: Sensor) -> str:
        self._update_state(percept)
        self._rule_match()
        return self._action.value

    def get_points(self) -> int:
        return self._state['Points']

    def _update_state(self, percept: Sensor) -> None:
        self._sensor_model = percept
        self._state['Environment'].state[self._sensor_model.name] = self._sensor_model.value

    def _rule_match(self) -> None:
        if self._state['Environment'].state[self._sensor_model.name] == 'Dirty':
            action = self._rules[self._sensor_model.value]
        else:
            action = self._rules[self._sensor_model.value][self._sensor_model.name]

        self._action.value = action
        self._state['Points'] += self._transition_model[self._action.value]
