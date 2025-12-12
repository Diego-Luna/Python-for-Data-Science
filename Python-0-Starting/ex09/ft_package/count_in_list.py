def count_in_list(lst: list, item) -> int:
    """
    Count occurrences of an item in a list.

    Args:
        lst: The list to search in
        item: The item to count

    Returns:
        Number of occurrences of item in lst

    Example:
        >>> count_in_list(["toto", "tata", "toto"], "toto")
        2
        >>> count_in_list(["toto", "tata", "toto"], "tutu")
        0
    """
    return lst.count(item)
