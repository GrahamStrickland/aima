#!/usr/bin/env python3
from copy import deepcopy

from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class ModelBasedReflexAgent:
    def __init__(self, possible_locations: list[str]):
        self._state = {
            'Environment': dict(
                (location, None) for locations in possible_locations for location in locations
            ),
            'Geography': possible_locations,
            'Points': 0
        }
        self._transition_model = {'Suck': 1,
                                  'Move': -1,
                                  'Stay': 0}
        self._sensor_model = Sensor(None, None)
        self._rules = {'Dirty': 'Suck', 
                       'Clean': 'Move',
                       'Blocked': 'Stay'},
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
        match self._rules[self._state['Environment'].state[self._sensor_model.name]]:
            case 'Suck':
                action = 'Suck'
            case 'Move':
                action = ""
            case 'Stay':
                action = 'Stay'

        self._action.value = action
        self._state['Points'] += self._transition_model[self._action.value]
