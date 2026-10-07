import os
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main() -> None:
    """Run tests for pimp_image filters."""
    # * Test subject case
    array = ft_load("../landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    # * Display docstring as specified in subject
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
