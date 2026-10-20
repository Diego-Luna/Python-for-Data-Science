from statistics import ft_statistics


def main() -> None:
    """Run tests for ft_statistics covering valid operations and errors."""
    # * Test mean, median, quartile
    ft_statistics(
        1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile"
    )
    print("-----")

    # * Test standard deviation and variance
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var"
    )
    print("-----")

    # * Test unrecognized kwargs (should not output anything)
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575,
        ejfhhe="heheh", ejdjdejn="kdekem"
    )
    print("-----")

    # ! Test empty arguments (should print ERROR for each valid request)
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
