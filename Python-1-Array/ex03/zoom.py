import os
import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    """Load animal.jpeg, crop 400x400 single-channel region, and display."""
    try:
        # * Locate animal image
        path = "animal.jpeg"
        if not os.path.exists(path):
            path = os.path.join(os.path.dirname(__file__), "..", "animal.jpeg")

        arr = ft_load(path)
        if arr is None:
            raise AssertionError("Could not load image.")

        print(arr)

        # * Crop 400x400 area with single channel (grayscale)
        sliced = arr[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {sliced.shape}")
        print(sliced)

        # * Display with matplotlib scale axes
        plt.imshow(sliced[:, :, 0], cmap="gray")
        plt.title("Zoom")
        plt.show()

    except Exception as e:
        # ! Safe error handling
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
