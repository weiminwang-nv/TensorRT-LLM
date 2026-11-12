"""Temporary probe for testing the Pyrefly diff workflow. Do not merge."""


def scale(value: int, factor: int) -> int:
    return value * factor


def run() -> int:
    return scale(1) + undefined_probe_name + another_undefined_name
