from ft_package import count_in_list


def main() -> None:
    """Verify count_in_list function output."""
    try:
        print(count_in_list(["toto", "tata", "toto"], "toto"))
        print(count_in_list(["toto", "tata", "toto"], "tutu"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
