from in_out import outer, pow, square


def main() -> None:
    """Run tests for outer closure and state mutation."""
    # * Test square transformation sequence
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")

    # * Test pow (self exponentiation) transformation sequence
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
