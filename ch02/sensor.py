#!/usr/bin/env python3
class Sensor:
    def __init__(self, name: str, percept: str):
        self.name = name
        self.percept = percept

    def __str__(self):
        return 'Sensor: {} = {}'.format(self.name, self.percept)
