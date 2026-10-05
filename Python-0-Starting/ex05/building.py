import sys
import string
from typing import Dict


def count_characters(text: str) -> Dict[str, int]:
    """Count character categories in a text.

    Args:
        text: The string to analyze.

    Returns:
        A dict with keys:
            'total','upper','lower','punctuation','spaces','digits'.
    """
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    return {
        'total': len(text),
        'upper': upper_count,
        'lower': lower_count,
        'punctuation': punctuation_count,
        'spaces': space_count,
        'digits': digit_count
    }


def display_counts(counts: Dict[str, int]) -> None:
    """Print the character counts in the format required by the exercise.

    Args:
        counts: Dictionary produced by :func:`count_characters`.
    """
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def get_text_from_args(argv: list) -> str:
    """Return the text to analyze from command-line arguments or stdin prompt.

    Args:
        argv: Command-line arguments list.

    Returns:
        The string to analyze.

    Raises:
        AssertionError: If more than one argument is provided.
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(argv) == 2 and argv[1]:
        return argv[1]

    print("What is the text to count?")
    try:
        return sys.stdin.readline()
    except (EOFError, KeyboardInterrupt):
        return ""


def main() -> None:
    """Program entry point: parse arguments and display character counts."""
    try:
        text = get_text_from_args(sys.argv)
        counts = count_characters(text)
        display_counts(counts)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
