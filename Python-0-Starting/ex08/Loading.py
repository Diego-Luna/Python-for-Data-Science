import os


def ft_tqdm(lst: range) -> None:
    """Mimic tqdm progress bar using yield.

    Args:
        lst: A range or iterable with known length.

    Yields:
        Each element from the range.
    """
    total = len(lst)
    if total == 0:
        return

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    for i, elem in enumerate(lst, start=1):
        percent = int((i / total) * 100)

        suffix = f"]| {i}/{total}"
        prefix = f"{percent:3d}%|["
        reserved = len(prefix) + len(suffix)
        bar_width = max(10, terminal_width - reserved)

        filled = int(bar_width * i / total)
        if filled >= bar_width:
            bar = '=' * (bar_width - 1) + '>'
        elif filled > 0:
            bar = '=' * (filled - 1) + '>'
        else:
            bar = ''

        spaces = ' ' * (bar_width - len(bar))
        output = f"\r{prefix}{bar}{spaces}{suffix}"

        print(output, end="", flush=True)
        yield elem
