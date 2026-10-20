from callLimit import callLimit


@callLimit(3)
def f() -> None:
    """Print identifier for function f."""
    print("f()")


@callLimit(1)
def g() -> None:
    """Print identifier for function g."""
    print("g()")


def main() -> None:
    """Run tests for callLimit decorator."""
    # * Iterate 3 times calling f and g
    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
