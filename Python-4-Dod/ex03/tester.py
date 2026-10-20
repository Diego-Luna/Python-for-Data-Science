from new_student import Student


def main() -> None:
    """Run tests for Student dataclass and immutable fields."""
    # * Test standard instantiation
    student = Student(name="Edward", surname="agle")
    print(student)

    # ! Test disallowed keyword argument initialization (id)
    try:
        Student(name="Edward", surname="agle", id="toto")
    except TypeError as e:
        print(f"TypeError: {e}")

    # ! Test disallowed keyword argument initialization (login)
    try:
        Student(name="Edward", surname="agle", login="toto")
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
