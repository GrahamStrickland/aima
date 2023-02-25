#!/usr/bin/env python3
from modules.actuator import Actuator
from modules.sensor import Sensor 


def reflex_vacuum_agent(location_status: Sensor) -> str:
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
