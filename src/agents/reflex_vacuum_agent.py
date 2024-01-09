#!/usr/bin/env python3
from ..data_structures import Actuator, Sensor


def reflex_vacuum_agent(location_status: Sensor) -> Actuator:
    location: str = location_status.name
    status: str = location_status.value

    action: str = ''
    if status == 'Dirty':
        action = 'Suck'
    elif location == 'A':
        action = 'Right'
    elif location == 'B':
        action = 'Left'

    return Actuator('action', action)

