"""A type error that already exists on the target branch. Its message names this module."""


def needs_one(x: int) -> int:
    return x


FIRST = needs_one()
