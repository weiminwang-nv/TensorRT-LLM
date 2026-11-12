"""Temporary probe for testing the Pyrefly check workflow. Do not merge."""


def scale(value: int, factor: int) -> int:
    return value * factor


def run() -> int:
    return scale(1, 2)
