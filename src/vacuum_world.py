#!/usr/bin/env python3
from agents.reflex_vacuum_agent import reflex_vacuum_agent
from modules.environment import Environment
from modules.sensor import Sensor


def main():
    print("Exercise 11: Reflex Vacuum Agent")

    task_environment = Environment('VacuumWorld', {'A': 'Dirty', 'B': 'Dirty'})
    location: str = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])
    print(task_environment)

    while task_environment.state != {'A': 'Clean', 'B': 'Clean'}:
        action: str = reflex_vacuum_agent(location_status).value

        if action == 'Suck':
            task_environment.state[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'
        else:
            raise SyntaxError("Invalid action string passed to agent.")

        location_status.name = location
        location_status.value = task_environment.state[location]
        print(task_environment)


if __name__ == '__main__':
    main()

