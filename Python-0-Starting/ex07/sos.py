import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def encode_to_morse(text: str) -> str:
    """
    Encode a string to Morse code using the NESTED_MORSE dictionary.

    Args:
        text: String containing only alphanumeric characters and spaces

    Returns:
        Morse code string with trailing space removed

    Raises:
        AssertionError: if text contains invalid characters
    """
    # * convert to uppercase for dictionary lookup
    text = text.upper()
    morse = ""

    for char in text:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse += NESTED_MORSE[char]

    # * remove trailing space
    return morse.rstrip()


def main() -> None:
    """
    Main program: convert command-line argument to Morse code.

    Expects exactly 1 argument containing only alphanumeric chars and spaces.
    Prints the Morse code representation.
    """
    try:
        # validate argument count
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        # * validate it's a string (redundant in Python but good practice)
        if not isinstance(text, str):
            raise AssertionError("the arguments are bad")

        # * encode and print
        morse_code = encode_to_morse(text)
        print(morse_code)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
