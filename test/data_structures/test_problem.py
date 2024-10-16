#!/usr/bin/env python3
"""Unit tests for Problem data structure."""

from src.data_structures import Problem


class TestProblem:
    def test_constructor(self, problem) -> None:
        assert isinstance(problem, Problem)

    def test_initial(self, problem: Problem) -> None:
        exp = "Arad"
        obs = problem.initial()

        assert obs == exp

        exp = "Zerind"
        obs = problem.initial()

        assert obs != exp

    def test_is_goal(self, problem: Problem) -> None:
        assert problem.is_goal("Bucharest")

        assert not problem.is_goal("Neamt")

    def test_actions(self, problem: Problem) -> None:
        assert problem.actions("Arad") == {"ToSibiu", "ToTimisoara", "ToZerind"}

    def test_result(self, problem: Problem) -> None:
        assert problem.result("Arad", "ToZerind") == "Zerind"

    def test_action_cost(self, problem: Problem) -> None:
        assert problem.action_cost("Arad", "ToZerind", "Zerind") == 75
