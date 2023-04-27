#!/usr/bin/env python3
from copy import deepcopy
from random import randint

from agents.model_based_reflex_agent import ModelBasedReflexAgent 
from agents.randomized_reflex_agent import RandomizedReflexAgent
from modules.environment import Environment
from modules.sensor import Sensor


def get_task_environments(
        possible_states: list[str], 
        possible_locations: list[list[str]],
        max_blocked: int
) -> list[Environment]:
    state = dict(
        (location, None) for locations in possible_locations for location in locations
    )

    num_locations = len(
        [location for locations in possible_locations for location in locations]
    )
    num_task_environments = num_locations**(len(possible_states)-1) * max_blocked

    task_environment = Environment(name='VacuumWorld', state=state)
    task_environments: list[Environment] = [
        deepcopy(task_environment) for _ in range(num_task_environments)
    ]

    return insert_random_states(possible_states, task_environments, max_blocked)


def insert_random_states(
        possible_states: list[str], 
        task_environments: list[Environment],
        max_blocked: int
) -> list[Environment]:

    for i in range(len(task_environments)):
        num_blocked = 0
        for location, _ in task_environments[i].state.items():
            curr_state = possible_states[randint(0, len(possible_states) - 1)]
            if curr_state == 'Blocked':
                num_blocked += 1
            while curr_state == 'Blocked' and num_blocked > max_blocked:
                curr_state = possible_states[randint(0, len(possible_states) - 1)]

            task_environments[i].state[location] = curr_state 

    return task_environments


def get_ideal_state(current_state: dict[str, str]) -> dict[str, str]:
    ideal_state = deepcopy(current_state)

    for location, value in ideal_state.items():
        if value != 'Blocked':
            ideal_state[location] = 'Clean'

    return ideal_state


def get_random_location(
        possible_locations: list[list[str]], state: dict[str, str]
) -> tuple[int]:
    row_num = randint(0, len(possible_locations) - 1)
    col_num = randint(0, len(possible_locations[0]) - 1)

    while state[possible_locations[row_num][col_num]] == 'Blocked':
        row_num = randint(0, len(possible_locations) - 1)
        col_num = randint(0, len(possible_locations[0]) - 1)

    return (row_num, col_num)


def get_action(
        agent, task_environment: Environment, possible_locations: list[list[str]],
        location_status: Sensor, row_num: int, col_num: int
) -> tuple[int]:
    action: str = agent.get_action(location_status)
    location = location_status.name

    new_row_num, new_col_num = row_num, col_num
    new_location = location_status.name

    if action == 'Suck':
        task_environment.state[location] = 'Clean'
    else:
        if action == 'Right':
            if col_num + 1 < len(possible_locations[0]):
                new_col_num = col_num + 1
        elif action == 'Left':
            if col_num - 1 >= 0:
                new_col_num = col_num - 1
        elif action == 'Up':
            if row_num - 1 >= 0:
                new_row_num = row_num - 1
        elif action == 'Down':
            if row_num + 1 < len(possible_locations):
                new_row_num = row_num + 1
        elif action == 'Stay':
            pass
        else:
            raise SyntaxError("Invalid action string passed to agent.")

        new_location = possible_locations[new_row_num][new_col_num]

        if task_environment.state[new_location] != 'Blocked':
            location = new_location 
            row_num = new_row_num
            col_num = new_col_num

    location_status.name = location
    location_status.value = task_environment.state[location]
    return (row_num, col_num)


def get_score(
        agent, task_environment: Environment, possible_locations: list[list[str]]
) -> int:
    ideal_state = get_ideal_state(task_environment.state)

    row_num, col_num = get_random_location(
        possible_locations, task_environment.state
    )
    location = possible_locations[row_num][col_num]
    location_status = Sensor(name=location, value=task_environment.state[location])
    curr_environment = deepcopy(task_environment)

    num_turns = 0
    while curr_environment.state != ideal_state:
        row_num, col_num = get_action(
            agent=agent, 
            task_environment=curr_environment, 
            possible_locations=possible_locations, 
            location_status=location_status, 
            row_num=row_num,
            col_num=col_num
        ) 
        num_turns += 1

    return num_turns


def main():
    print("Exercise 14: Vacuum Unknown Geography\n")

    possible_states = ['Dirty', 'Clean', 'Blocked']
    possible_locations = [['A', 'B'], 
                          ['C', 'D']]
    max_blocked = 1 # having more than one blocked state in a 2x2 grid can cause
                    # deadlock, since agent cannot move diagonally

    task_environments: list[Environment] = get_task_environments(
        possible_states, possible_locations, max_blocked
    )
    simple_scores: list[int] = []
    stateful_scores: list[int] = []

    simple_agent = RandomizedReflexAgent()
    stateful_agent = ModelBasedReflexAgent(possible_locations=possible_locations)

    for task_environment in task_environments:
        score = get_score(
            agent=simple_agent, 
            task_environment=task_environment, 
            possible_locations=possible_locations
        )
        simple_scores.append(score)

        score = get_score(
            agent=stateful_agent, 
            task_environment=task_environment, 
            possible_locations=possible_locations
        )
        stateful_scores.append(score)

    print(
        "Overall average score for simple agent: ", 
        sum(simple_scores) / len(simple_scores)
    )
    print(
        "Overall average score for stateful agent: ", 
        sum(stateful_scores) / len(stateful_scores)
    )


if __name__ == '__main__':
    main()
