#!/usr/bin/env python3
class Actuator:
    def __init__(self, name: str, action: str):
        self.name = name
        self.action = action

    def __str__(self):
        return 'Actuator: {} = {}'.format(self.name, self.action)
