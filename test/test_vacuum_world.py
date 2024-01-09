#!/usr/bin/env python3
from copy import deepcopy

from src.agents import reflex_vacuum_agent
from src.data_structures import Actuator, Environment, Sensor 


def test_vacuum_world() -> None:
    task_environment = Environment('VacuumWorld', {'A': 'Clean', 'B': 'Clean'})
    location: str = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])

    exp = [{'A': 'Clean', 'B': 'Clean'}]
    obs: list(dict(str, str)) = [deepcopy(task_environment.state)]

    while task_environment.state != exp[-1]:
        action: str = reflex_vacuum_agent(location_status).value

        if action == 'Suck':
            task_environment.state[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'

        location_status.name = location
        location_status.value = task_environment.state[location]
        obs.append(deepcopy(task_environment.state))

    assert obs == exp


def test_vacuum_world2() -> None:
    task_environment = Environment('VacuumWorld', {'A': 'Dirty', 'B': 'Clean'})
    location: str = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])

    exp = [{'A': 'Dirty', 'B': 'Clean'},
           {'A': 'Clean', 'B': 'Clean'}]
    obs: list(dict(str, str)) = [deepcopy(task_environment.state)]

    while task_environment.state != exp[-1]:
        action: str = reflex_vacuum_agent(location_status).value

        if action == 'Suck':
            task_environment.state[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'

        location_status.name = location
        location_status.value = task_environment.state[location]
        obs.append(deepcopy(task_environment.state))

    assert obs == exp


def test_vacuum_world3() -> None:
    task_environment = Environment('VacuumWorld', {'A': 'Clean', 'B': 'Dirty'})
    location: str = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])

    exp = [{'A': 'Clean', 'B': 'Dirty'},
           {'A': 'Clean', 'B': 'Dirty'},
           {'A': 'Clean', 'B': 'Clean'}]
    obs: list(dict(str, str)) = [deepcopy(task_environment.state)]

    while task_environment.state != exp[-1]:
        action: str = reflex_vacuum_agent(location_status).value

        if action == 'Suck':
            task_environment.state[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'

        location_status.name = location
        location_status.value = task_environment.state[location]
        obs.append(deepcopy(task_environment.state))

    assert obs == exp


def test_vacuum_world4() -> None:
    task_environment = Environment('VacuumWorld', {'A': 'Dirty', 'B': 'Dirty'})
    location: str = 'A'
    location_status = Sensor(name=location, value=task_environment.state[location])

    exp = [{'A': 'Dirty', 'B': 'Dirty'},
           {'A': 'Clean', 'B': 'Dirty'},
           {'A': 'Clean', 'B': 'Dirty'},
           {'A': 'Clean', 'B': 'Clean'}]
    obs: list(dict(str, str)) = [deepcopy(task_environment.state)]

    while task_environment.state != exp[-1]:
        action: str = reflex_vacuum_agent(location_status).value

        if action == 'Suck':
            task_environment.state[location] = 'Clean'
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'

        location_status.name = location
        location_status.value = task_environment.state[location]
        obs.append(deepcopy(task_environment.state))

    assert obs == exp
