#!/usr/bin/env python3
from copy import deepcopy

from ..agents import ModelBasedReflexAgent
from ..data_structures import Environment, Sensor


# noinspection DuplicatedCode
def main():
    print("Exercise 13: Vacuum Motion Penalty\n")

    agent = ModelBasedReflexAgent()
    task_environment = Environment("VacuumWorld", {"A": "Dirty", "B": "Dirty"})
    states: list[str] = ["Dirty", "Clean"]
    locations: list[str] = ["A", "B"]
    task_environments: list[Environment] = [
        deepcopy(task_environment) for _ in range(len(states) ** 2 * len(locations))
    ]
    scores: list[int] = []

    for i in range(1, len(task_environments)):
        task_environments[i].state = {
            "A": states[(i // 2) >> 1],
            "B": states[(i // 2) & 1],
        }

    i = 0
    for task_environment in task_environments:
        num_turns = 0
        location = locations[i % 2]

        location_status = Sensor(name=location, value=task_environment.state[location])
        print(f"Simulation {i+1}")
        print(f"Starting task environment: {task_environment.state}")
        print(f"Agent start location: {location}")

        while task_environment.state != {"A": "Clean", "B": "Clean"}:
            action: str = agent.get_action(location_status)
            num_turns += 1

            if action == "Suck":
                task_environment.state[location] = "Clean"
            elif action == "Right":
                location = "B"
            elif action == "Left":
                location = "A"
            else:
                raise SyntaxError("Invalid action string passed to agent.")

            location_status.name = location
            location_status.value = task_environment.state[location]
            print(f"After turn {num_turns}: {task_environment.state}")

        print(f"Performance score for configuration: {num_turns}\n")

        score: int = num_turns - agent.get_points()
        scores.append(score if score >= 0 else 0)
        i += 1

    print("Overall average score: ", sum(scores) / len(scores))


if __name__ == "__main__":
    main()
