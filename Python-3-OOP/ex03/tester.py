from ft_calculator import calculator


def main() -> None:
    """Run tests for vector-scalar operator overloading."""
    # * Test addition
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")

    # * Test multiplication
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")

    # * Test subtraction and division
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5

    # ! Test division by zero
    print("---")
    v3 / 0
    v3 * 0
    v3 + 0
    v3 - 0


if __name__ == "__main__":
    main()
