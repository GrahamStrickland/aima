#!/usr/bin/env python3


class Environment:
    def __init__(self, name: str, state: dict[str, str]):
        self.name = name
        self.state = state

    def __str__(self):
        return 'Environment: {} = {}'.format(self.name, self.state)
