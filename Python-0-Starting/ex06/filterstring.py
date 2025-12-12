import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main program: filter words from string S with length > N.

    Expects exactly 2 arguments: a string and an integer.
    Prints the filtered list of words.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        # * validate types: arg1 must be string, arg2 must be convertible (int)
        if not isinstance(arg1, str):
            raise AssertionError("the arguments are bad")

        try:
            n = int(arg2)
        except ValueError:
            raise AssertionError("the arguments are bad")

        # * split string into words
        words = arg1.split()

        filtered = ft_filter(lambda word: len(word) > n, words)

        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
