from S1E9 import Character, Stark


def main() -> None:
    """Run tests for Character abstract class and Stark concrete class."""
    # * Test subject case: Stark initialization and death
    ned = Stark("Ned")
    print(ned.__dict__)
    print(ned.is_alive)
    ned.die()
    print(ned.is_alive)
    print(ned.__doc__)
    print(ned.__init__.__doc__)
    print(ned.die.__doc__)
    print("---")

    # * Test Stark with is_alive set to False
    lyanna = Stark("Lyanna", False)
    print(lyanna.__dict__)

    # ! Verify that instantiating abstract Character directly raises TypeError
    try:
        Character("hodor")
        print("Error: Character instantiation should have failed")
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
