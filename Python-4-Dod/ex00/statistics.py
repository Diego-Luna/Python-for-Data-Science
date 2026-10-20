from typing import Any


def calculate_mean(data: list[int | float]) -> float:
    """Calculate arithmetic mean of a numerical dataset."""
    return sum(data) / len(data)


def calculate_median(sorted_data: list[int | float]) -> int | float:
    """Calculate median value from sorted numerical data."""
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def calculate_quartile(sorted_data: list[int | float]) -> list[float]:
    """Calculate 25% and 75% quartiles from sorted data."""
    n = len(sorted_data)
    q1 = float(sorted_data[int(n * 0.25)])
    q3 = float(sorted_data[int(n * 0.75)])
    return [q1, q3]


def calculate_var(data: list[int | float], mean: float) -> float:
    """Calculate population variance of data."""
    return sum((x - mean) ** 2 for x in data) / len(data)


def calculate_std(variance: float) -> float:
    """Calculate standard deviation from variance."""
    return variance ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and display requested statistics from variable arguments."""
    valid_requests = {"mean", "median", "quartile", "std", "var"}

    # ! Validate that numerical data exists
    if len(args) == 0:
        for val in kwargs.values():
            if val in valid_requests:
                print("ERROR")
        return

    # ! Verify all elements are numeric
    for x in args:
        if not isinstance(x, (int, float)):
            for val in kwargs.values():
                if val in valid_requests:
                    print("ERROR")
            return

    sorted_data = sorted(args)
    mean_val = calculate_mean(sorted_data)
    var_val = calculate_var(sorted_data, mean_val)

    # * Dispatch calculations based on keyword arguments
    for val in kwargs.values():
        if val == "mean":
            print(f"mean : {mean_val}")
        elif val == "median":
            print(f"median : {calculate_median(sorted_data)}")
        elif val == "quartile":
            print(f"quartile : {calculate_quartile(sorted_data)}")
        elif val == "std":
            print(f"std : {calculate_std(var_val)}")
        elif val == "var":
            print(f"var : {var_val}")
