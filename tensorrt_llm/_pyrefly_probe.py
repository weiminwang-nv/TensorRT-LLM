"""Temporary probe for testing the Pyrefly diff workflow. Do not merge."""

import numpy as np
from pydantic import BaseModel


class Probe(BaseModel):
    value: int = 0


def scale(value: int, factor: int) -> int:
    return value * factor


def run() -> int:
    data = np.zeros(3)
    return scale(len(data)) + undefined_probe_name
