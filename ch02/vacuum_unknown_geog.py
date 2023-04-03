#!/usr/bin/env python3
from copy import deepcopy
from random import randint
from pdb import set_trace

from agents.randomized_reflex_agent import RandomizedReflexAgent
from modules.environment import Environment
from modules.sensor import Sensor


def get_task_environments(possible_states: list[str], possible_locations: list[list[str]]) -> list[Environment]:
    state = dict((location, None) for locations in possible_locations for location in locations)

    num_locations = len([location for locations in possible_locations for location in locations])

    task_environment = Environment('VacuumWorld', state)
    task_environments: list[Environment] = [
        deepcopy(task_environment) for _ in range(num_locations**len(possible_states))
    ]

    return insert_random_states(possible_states, task_environments)


def insert_random_states(
        possible_states: list[str], task_environments: list[Environment]
) -> list[Environment]:
    blocked_task_environment = deepcopy(task_environments[0])
    for location, _ in blocked_task_environment.state.items():
        blocked_task_environment.state[location] = 'Blocked'

    for i in range(len(task_environments)):
        for location, _ in task_environments[i].state.items():
            task_environments[i].state[location] = possible_states[randint(0, len(possible_states) - 1)]
        if task_environments[i] == blocked_task_environment:
            i -= 1

    return task_environments


def get_ideal_state(current_state: dict[str, str]) -> dict[str, str]:
    ideal_state = deepcopy(current_state)

    for location, value in ideal_state.items():
        if value != 'Blocked':
            ideal_state[location] = 'Clean'

    return ideal_state


def get_random_location(possible_locations: list[list[str]], state: dict[str, str]) -> tuple[int]:
    row_num = randint(0, len(possible_locations[0]) - 1)
    col_num = randint(0, len(possible_locations) - 1)

    while state[possible_locations[row_num][col_num]] == 'Blocked':
        row_num = randint(0, len(possible_locations[0]) - 1)
        col_num = randint(0, len(possible_locations) - 1)

    return (row_num, col_num)


def main():
    print("Exercise 14: Vacuum Unknown Geography\n")

    agent = RandomizedReflexAgent()
    possible_states = ['Dirty', 'Clean', 'Blocked']
    possible_locations = [['A', 'B'],
                          ['C', 'D']]

    task_environments: list[Environment] = get_task_environments(possible_states, possible_locations)
    scores: list[int] = []

    for task_environment in task_environments:
        print("Executing task environment: ", task_environment.state)

        ideal_state = get_ideal_state(task_environment.state)

        row_num, col_num = get_random_location(possible_locations, task_environment.state)
        location = possible_locations[row_num][col_num]
        location_status = Sensor(name=location, value=task_environment.state[location])

        num_turns = 0
        while task_environment.state != ideal_state:
            set_trace()

            action: str = agent.get_action(location_status)

            new_row_num, new_col_num = row_num, col_num
            new_location = location
            num_turns += 1

            if action == 'Suck':
                task_environment.state[location] = 'Clean'
            else:
                if action == 'Right':
                    if col_num + 1 < len(possible_locations):
                        new_col_num = col_num + 1
                elif action == 'Left':
                    if col_num - 1 >= 0:
                        new_col_num = col_num - 1
                elif action == 'Up':
                    if row_num - 1 >= 0:
                        new_row_num = row_num - 1
                elif action == 'Down':
                    if row_num + 1 > len(possible_locations[0]):
                        new_row_num = row_num + 1
                else:
                    raise SyntaxError("Invalid action string passed to agent.")

                new_location = possible_locations[new_row_num][new_col_num]

                if task_environment.state[new_location] != 'Blocked':
                    location = new_location 
                    row_num = new_row_num
                    col_num = new_col_num

            location_status.name = location
            location_status.value = task_environment.state[location]

        scores.append(num_turns)

    print("Overall average score: ", sum(scores) / len(scores))


if __name__ == '__main__':
    main()
