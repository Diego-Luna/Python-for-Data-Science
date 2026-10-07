import os
from load_image import ft_load


def main() -> None:
    """Run tests for ft_load."""
    # * Test valid subject image
    img_path = os.path.join(os.path.dirname(__file__), "..", "landscape.jpg")

    print(ft_load(img_path))

    # ! Test invalid cases
    print(ft_load("missing.jpg"))
    print(ft_load(42))


if __name__ == "__main__":
    main()
