def NULL_not_found(object: any) -> int:
    """Print the object type of all types of Null.

    Args:
        object: The object to inspect.

    Returns:
        0 if a null-equivalent type is detected, 1 otherwise.
    """
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0

    if isinstance(object, float) and object != object:
        print(f"Cheese: nan {type(object)}")
        return 0

    if type(object) is int and object == 0:
        print(f"Zero: 0 {type(object)}")
        return 0

    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0

    if isinstance(object, bool) and object is False:
        print(f"Fake: False {type(object)}")
        return 0

    print("Type not Found")
    return 1
