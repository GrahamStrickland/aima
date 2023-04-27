#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor


class ModelBasedReflexAgent:
    def __init__(self, possible_locations: list[list[str]]):
        self._state = {
            'Environment': Environment(
                name='VacuumWorld', 
                state=dict(
                    (location, None) for locations in possible_locations for location in locations
                )
            ),
            'Geography': possible_locations,
            'Current': None,
            'Points': 0
        }
        self._transition_model = {'Suck': 1,
                                  'Move': -1,
                                  'Stay': 0}
        self._sensor_model = Sensor(None, None)
        self._rules = {'Dirty': 'Suck', 
                       'Clean': ['Up', 'Right', 'Down', 'Left'],
                       'Blocked': 'Stay'}
        self._action = Actuator('action', None)

    def get_action(self, percept: Sensor) -> str:
        self._update_state(percept)
        self._rule_match()
        return self._action.value

    def get_points(self) -> int:
        return self._state['Points']

    def _update_state(self, percept: Sensor) -> None:
        self._sensor_model = percept
        self._state['Current'] = self._sensor_model.name
        self._state['Environment'].state[self._sensor_model.name] = self._sensor_model.value

    def _rule_match(self) -> None:
        curr = self._state['Current']
        state = self._state['Environment'].state
        action = ''

        match self._rules[state[curr]]:
            case 'Suck':
                action = 'Suck'
            case 'Move':
                possible_locations = self._state['Geography']
                row_num = self._state['CurrentRowNum']
                col_num = self._state['CurrentColNum']
                next = possible_locations[row_num][col_num]
                for move in self._rules['Clean']:
                    match move:
                        case 'Up':
                            if row_num - 1 >= 0 and state[next] != 'Blocked':
                                action = move
                                break
                        case 'Right':
                            if col_num + 1 < len(possible_locations[0]) and state[next] != 'Blocked':
                                action = move
                                break
                        case 'Down':
                            if row_num + 1 < len(possible_locations) and state[next] != 'Blocked':
                                action = move
                                break
                        case 'Left':
                            if col_num - 1 >= 0 and state[next] != 'Blocked':
                                action = move
                                break
            case 'Stay':
                action = 'Stay'

        self._action.value = action
        self._state['Points'] += self._transition_model[self._action.value]
