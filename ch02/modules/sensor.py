#!/usr/bin/env python3


class Sensor:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value 

    def __str__(self):
        return 'Sensor: {} = {}'.format(self.name, self.value)
