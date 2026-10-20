from typing import Any


def square(x: int | float) -> int | float:
    """Return the square of a given numerical argument."""
    # * Compute square of x
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of argument by itself."""
    # * Compute x raised to the power of x
    return x ** x


def outer(x: int | float, function: Any) -> object:
    """Return a closure object that repeatedly applies function to state."""
    count = 0

    def inner() -> float:
        """Apply function to inner variable state and update accumulator."""
        nonlocal count, x
        # * Increment counter and update state by evaluating function
        count += 1
        x = function(x)
        return x

    return inner
