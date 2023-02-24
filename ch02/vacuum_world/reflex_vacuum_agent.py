#!/usr/bin/env python3
from ..environment import Environment
from ..actuator import Actuator


def reflex_vacuum_agent(inputs: list[str, str]) -> str:
    location = inputs[0]
    status = inputs[1]
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'


def main():
    print("Exercise 11: Reflex Vacuum Agent")

    task_environment = Environment('VacuumWorld', {'A': 'Clean', 'B': 'Dirty'})

    while task_environment.state != {'A': 'Clean', 'B': 'Clean'}:
        print(task_environment)
        reflex_vacuum_agent
