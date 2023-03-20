#!/usr/bin/env python3
from copy import deepcopy

from agents.reflex_vacuum_agent import reflex_vacuum_agent
from modules.environment import Environment
from modules.sensor import Sensor


def main():
    print("Exercise 12: Simple Reflex Agent Scoring")

    task_environment = Environment('VacuumWorld', {'A': 'Dirty', 'B': 'Dirty'})
    states: list[str] = ['Dirty', 'Clean']
    locations: list[str] = ['A', 'B']
    task_environments: list[Environment] = [
        deepcopy(task_environment) for _ in range(len(states)**2 * len(locations))
    ]
    scores: list[int] = []
    location = locations[0]

    for i in range(1, len(task_environments)):
        if i % 2 == 0:
            task_environments[i].state = {'A': states[(i//2) >> 1], 'B': states[(i//2) & 1]}

    while len(scores) < len(task_environments):
        num_turns = 0
        location = locations[1] if location == locations[0] else locations[0]

        location_status = Sensor(name=location, value=task_environment.state[location])
        print(task_environment)

        while task_environment.state != {'A': 'Clean', 'B': 'Clean'}:
            action: str = reflex_vacuum_agent(location_status).value
            num_turns += 1

            if action == 'Suck':
                task_environment.state[location] = 'Clean'
            elif action == 'Right':
                location = 'B'
            elif action == 'Left':
                location = 'A'

            location_status.name = location
            location_status.value = task_environment.state[location]
            print(task_environment)

        print("Performance score for configuration: ", num_turns)
        scores.append(num_turns)

    print("Overall average score: ", sum(scores) / len(scores))


if __name__ == '__main__':
    main()
