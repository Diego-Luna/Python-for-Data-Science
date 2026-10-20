from S1E7 import Baratheon, Lannister


def main() -> None:
    """Run tests for Baratheon and Lannister families."""
    # * Test Baratheon character
    robert = Baratheon("Robert")
    print(robert.__dict__)
    print(robert.__str__)
    print(robert.__repr__)
    print(robert.is_alive)
    robert.die()
    print(robert.is_alive)
    print(robert.__doc__)
    print("---")

    # * Test Lannister character
    cersei = Lannister("Cersei")
    print(cersei.__dict__)
    print(cersei.__str__)
    print(cersei.is_alive)
    print("---")

    # * Test class method chain creation
    jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"Name : {(jaine.first_name, type(jaine).__name__)}, "
        f"Alive : {jaine.is_alive}"
    )


if __name__ == "__main__":
    main()
