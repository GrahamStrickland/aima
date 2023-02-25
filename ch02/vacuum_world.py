#!/usr/bin/env python3
from agents.reflex_vacuum_agent import reflex_vacuum_agent
from modules.actuator import Actuator
from modules.environment import Environment
from modules.sensor import Sensor 


def main():
    print("Exercise 11: Reflex Vacuum Agent")

    task_environment = Environment('VacuumWorld', {'A': 'Clean', 'B': 'Clean'})
    location = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])
    print(task_environment)

    while task_environment.state != {'A': 'Clean', 'B': 'Clean'}:
        response: str = reflex_vacuum_agent(location_status).value

        if response == 'Suck':
            task_environment.state[location] = 'Clean'
        elif response == 'Right':
            location = 'B'
        elif response == 'Left':
            location = 'A'

        location_status.name = location
        location_status.value = task_environment.state[location]
        print(task_environment)


if __name__ == '__main__':
    main()
