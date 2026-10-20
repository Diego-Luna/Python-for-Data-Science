from typing import Any


def callLimit(limit: int) -> Any:
    """Decorator factory to block function execution beyond a call limit."""
    count = 0

    def callLimiter(function: Any) -> Any:
        """Wrap target function to track invocations."""

        def limit_function(*args: Any, **kwds: Any) -> Any:
            """Check execution counter against limit and invoke function."""
            nonlocal count
            # * Execute function if within limit count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            # ! Block execution and report limit exceeded
            print(f"Error: {function} call too many times")
            return None

        return limit_function

    return callLimiter
