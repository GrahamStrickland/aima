#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class ModelBasedReflexAgent:
    def __init__(self):
        self._state = Environment('None', {})
        self._transition_model = {}
        self._sensor_model = {}
        self._rules = {'Dirty': 'Suck',
                       'Clean': {
                           'A': 'Right',
                           'B': 'Left'
                           }
                       }
        self._action = Actuator('action', 'none')

    def _update_state(self, percept: Sensor) -> None:
        pass

    def _rule_match(self) -> None:
        pass

    def get_action(self, percept: Sensor) -> str:
        return self._action.value
