#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class ModelBasedReflexAgent:
    def __init__(self):
        self._state = {'Environment': Environment('VacuumWorld', {'A': None, 'B': None}),
                       'Points': 0}
        self._transition_model = {'Suck': 0,
                                  'Right': -1,
                                  'Left': -1}
        self._sensor_model = Environment('VacuumWorld', {'A': None, 'B': None})
        self._rules = {'Dirty': 'Suck',
                       'Clean': {
                           'A': 'Right',
                           'B': 'Left'
                           }
                       }
        self._action = Actuator('action', 'none')

    def get_action(self, percept: Sensor) -> str:
        self._update_state(percept)
        self._rule_match()
        return self._action.value

    def _update_state(self, percept: Sensor) -> None:
        self._sensor_model.state[percept.name] = percept.value

    def _rule_match(self) -> None:
        pass
