#!/usr/bin/env python3
from copy import deepcopy
from random import randint

from agents.model_based_reflex_agent import ModelBasedReflexAgent
from modules.environment import Environment
from modules.sensor import Sensor


def get_task_environments(possible_states: list[str], possible_locations: list[list[str]]) -> list[Environment]:
    state = dict((location, None) for locations in possible_locations for location in locations)

    num_locations = len([location for locations in possible_locations for location in locations])

    task_environment = Environment('VacuumWorld', state)
    task_environments: list[Environment] = [
        deepcopy(task_environment) for _ in range(len(possible_states)**num_locations)
    ]

    return insert_random_states(possible_states, task_environments)


def insert_random_states(
        possible_states: list[str], task_environments: list[Environment]
) -> list[Environment]:
    for task_environment in task_environments:
        for location, _ in task_environment.state.items():
            task_environment.state[location] = possible_states[randint(1, len(possible_states))]

    return task_environments


def main():
    print("Exercise 14: Vacuum Unknown Geography\n")

    agent = ModelBasedReflexAgent()
    possible_states = ['Dirty', 'Clean', 'Blocked']
    possible_locations = [['A', 'B'],
                          ['C', 'D']]

    task_environments: list[Environment] = get_task_environments(possible_states, possible_locations)
    scores: list[int] = []

    for task_environment in task_environments:
        num_turns = 0
        location = possible_locations[randint(range(len(possible_locations)**2))]

        location_status = Sensor(name=location, value=task_environment.state[location])

        while task_environment.state != {'A': 'Clean', 'B': 'Clean'}:
            action: str = agent.get_action(location_status)
            num_turns += 1

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

        score: int = num_turns - agent.get_points()
        scores.append(score if score >= 0 else 0)

    print("Overall average score: ", sum(scores) / len(scores))


if __name__ == '__main__':
    main()
