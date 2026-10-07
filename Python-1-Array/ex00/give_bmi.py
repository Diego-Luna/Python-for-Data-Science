import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""

    # ! validate input types and dimensions
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("Inputs must be lists.")
    if len(height) != len(weight):
        raise AssertionError("Lists must have the same size.")

    # ! verify elements are valid positive numbers
    for h in height:
        if not isinstance(h, (int, float)) or isinstance(h, bool) or h <= 0:
            raise AssertionError("Heights must be positive numbers.")
    for w in weight:
        if not isinstance(w, (int, float)) or isinstance(w, bool) or w <= 0:
            raise AssertionError("Weights must be positive numbers.")

    # * vectorized BMI calculation: weight / height ** 2

    h_arr = np.array(height, dtype=float)
    w_arr = np.array(weight, dtype=float)
    bmi = w_arr / (h_arr ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Determine whether BMI values exceed a limit."""
    # ! Validate parameter types
    if not isinstance(bmi, list):
        raise AssertionError("BMI values must be a list.")
    if not isinstance(limit, (int, float)) or isinstance(limit, bool):
        raise AssertionError("Limit must be an integer or float.")

    for val in bmi:
        if not isinstance(val, (int, float)) or isinstance(val, bool):
            raise AssertionError("BMI values must be numbers.")

    # * Filter values strictly greater than limit
    return [val > limit for val in bmi]
