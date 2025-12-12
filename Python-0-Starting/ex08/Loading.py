import os
import sys


def ft_tqdm(lst: range) -> None:
    """
    Mimics tqdm progress bar using yield.

    Displays a progress bar with percentage, visual bar, and counter.
    Updates on the same line using carriage return.

    Args:
        lst: A range object to iterate over

    Yields:
        Each element from the range
    """
    total = len(lst)

    # * get terminal width, default to 80 if not available
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    for i, elem in enumerate(lst, start=1):
        percent = (i / total) * 100

        reserved = 50
        bar_width = max(10, terminal_width - reserved)

        # * create progress bar
        filled = int(bar_width * i / total)
        bar = '=' * filled + '>' if filled < bar_width else '=' * bar_width
        spaces = ' ' * (bar_width - len(bar))

        output = f"\r{percent:3.0f}%|[{bar}{spaces}]| {i}/{total}"

        sys.stdout.write(output)
        sys.stdout.flush()

        yield elem

    # ! final newline after completion
    sys.stdout.write('\n')
    sys.stdout.flush()
