import sys
import string
from ft_filter import ft_filter


def main() -> None:
    """Filter words from string S that have length greater than N."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        try:
            n = int(arg2)
        except ValueError:
            raise AssertionError("the arguments are bad")

        if any(c in string.punctuation for c in arg1):
            raise AssertionError("the arguments are bad")

        if any(
            not c.isprintable() or (c.isspace() and c != ' ') for c in arg1
        ):
            raise AssertionError("the arguments are bad")

        words = arg1.split()
        filtered = [word for word in ft_filter(lambda w: len(w) > n, words)]
        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
