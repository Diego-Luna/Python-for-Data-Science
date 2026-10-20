from DiamondTrap import King


def main() -> None:
    """Run tests for diamond inheritance and property modifications."""
    # * Test subject case: King initialization and trait modification
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)


if __name__ == "__main__":
    main()
