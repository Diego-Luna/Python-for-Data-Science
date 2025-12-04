import sys
import string
from typing import Dict


def count_characters(text: str):
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    # * Iterate once, classify each character with clear rules.
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char == ' ':
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


def display_counts(counts: Dict[str, int]):
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def get_text_from_args(argv: list):
    # ! If user explicitly asks for tests, return a sentinel
    if len(argv) == 2 and argv[1] == "--test":
        return "__RUN_TESTS__"

    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(argv) == 2:
        return argv[1]

    try:
        return input("What is the text to count?\n")
    except (EOFError, KeyboardInterrupt):
        return ""


def main():
    try:
        text = get_text_from_args(sys.argv)
        if text == "__RUN_TESTS__":
            run_tests()
            return

        counts = count_characters(text)
        display_counts(counts)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


def run_tests():
    samples = [
        "Hello World!",
        "Python 3.0, released in 2008.",
    ]

    for s in samples:
        print(f"Sample: {s}")
        counts = count_characters(s)
        display_counts(counts)
        print('')


if __name__ == "__main__":
    main()
