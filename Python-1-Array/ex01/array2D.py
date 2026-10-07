import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print shape of 2D array and return sliced portion along rows."""
    # ! Validate input format and indices
    if not isinstance(family, list):
        raise AssertionError("Input must be a list.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("Indices must be integers.")

    if len(family) > 0:
        if not all(isinstance(row, list) for row in family):
            raise AssertionError("All elements must be lists.")
        row_len = len(family[0])
        if not all(len(row) == row_len for row in family):
            raise AssertionError("All rows must have the same length.")

    # * Print initial shape and sliced shape
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")

    return sliced.tolist()
