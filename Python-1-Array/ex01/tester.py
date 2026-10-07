from array2D import slice_me


def main() -> None:
    """Run tests for slice_me."""
    # * Test subject cases
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # ! Test invalid inputs
    try:
        slice_me([[1.80, 78.4], [2.15]], 0, 1)
    except AssertionError as e:
        print(f"AssertionError: {e}")

    try:
        slice_me("not a list", 0, 1)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
