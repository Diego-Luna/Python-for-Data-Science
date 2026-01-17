def NULL_not_found(object: any) -> int:
    # * None type
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    
    # * NaN (float)
    if isinstance(object, float) and object != object:  # ! NaN != NaN is True
        print(f"Cheese: nan {type(object)}")
        return 0
    
    # * Zero (int) - check type to distinguish from False
    if isinstance(object, int) and object == 0 and object is not False:
        print(f"Zero: 0 {type(object)}")
        return 0
    
    # * Empty string
    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0
    
    # * False (bool)
    if isinstance(object, bool) and object is False:
        print(f"Fake: False {type(object)}")
        return 0
    
    # * Type not found
    print("Type not Found")
    return 1
