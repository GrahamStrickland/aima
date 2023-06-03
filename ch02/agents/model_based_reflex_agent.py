#!/usr/bin/env python3
from random import randint

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
            'Next': None,
            'Points': 0
        }
        self._transition_model = {'Suck': 1,
                                  'Move': -1}
        self._sensor_model = Sensor(None, None)
        self._rules = {'Dirty': 'Suck', 
                       'Clean': 'Move',
                       'Blocked': 'Stay'}
        self._action = Actuator('action', None)
        self._directions = ['Up', 'Right', 'Down', 'Left']
        self._direction = 0

    def get_action(self, percept: Sensor) -> str:
        self._update_state(percept)
        self._rule_match()
        return self._action.value

    def get_points(self) -> int:
        return self._state['Points']

    def _update_state(self, percept: Sensor) -> None:
        self._sensor_model = percept

        if self._state['Current'] == self._sensor_model.name and self._action.value in self._directions:
            self._state['Environment'].state[self._state['Next']] = 'Blocked' 

        self._state['Current'] = self._sensor_model.name
        self._state['Environment'].state[self._sensor_model.name] = self._sensor_model.value

    def _get_next_position(self, move: str, row_num: int, col_num: int) -> str:
        possible_locations = self._state['Geography']

        match move:
            case 'Up':
                if row_num - 1 >= 0:
                    return possible_locations[row_num-1][col_num]
            case 'Right':
                if col_num + 1 < len(possible_locations[0]):
                    return possible_locations[row_num][col_num+1]
            case 'Down':
                if row_num + 1 < len(possible_locations):
                    return possible_locations[row_num+1][col_num]
            case 'Left':
                if col_num - 1 >= 0:
                    return possible_locations[row_num][col_num-1]
        
        return possible_locations[row_num][col_num]
    
    def _get_current_position(self, curr: str) -> tuple[int]:
        possible_locations = self._state['Geography']

        for row_num in range(len(possible_locations)):
            for col_num in range(len(possible_locations[row_num])):
                if possible_locations[row_num][col_num] == curr:
                    return (row_num, col_num)

        raise IndexError("Incorrect row and column reference")

    def _rule_match(self) -> None:
        curr = self._state['Current']
        state = self._state['Environment'].state
        action = self._rules[state[curr]]

        if action == 'Move':
            row_num, col_num = self._get_current_position(curr)

            while action == 'Move':
                move = self._directions[self._direction]
                next = self._get_next_position(move, row_num, col_num)
                self._state['Next'] = next
                if next != curr and state[next] != ('Blocked' or 'Clean'):
                    action = move
                else:
                    self._direction = randint(0, len(self._directions) - 1)

        self._action.value = action
        if action in self._directions:
            self._state['Points'] += self._transition_model['Move']
        else:
            self._state['Points'] += self._transition_model[self._action.value]
