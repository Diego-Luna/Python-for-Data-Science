import os
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D matrix manually without using library functions."""
    rows = len(array)
    cols = len(array[0])
    # * Transpose by swapping coordinates manually
    transposed = [
        [array[row][col] for row in range(rows)]
        for col in range(cols)
    ]
    return np.array(transposed)


def main() -> None:
    """Load image, crop square, transpose manually, and display."""
    try:
        path = "animal.jpeg"
        if not os.path.exists(path):
            path = os.path.join(os.path.dirname(__file__), "..", "animal.jpeg")

        arr = ft_load(path, verbose=False)
        if arr is None:
            raise AssertionError("Could not load image.")

        # * 400x400 square region with coordinate orientation matching
        # * subject: Axis 0 traverses X (450:850), Axis 1 traverses Y (100:500)
        sliced = np.array([
            [[arr[y][x][0]] for y in range(100, 500)]
            for x in range(450, 850)
        ])
        print(f"The shape of image is: {sliced.shape} or {sliced.shape[::-1]}")
        print(sliced)

        # * Transpose manually without using numpy transpose / .T
        sq = sliced[:, :, 0]
        transposed = manual_transpose(sq)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # * Display transposed result
        plt.imshow(transposed, cmap="gray")
        plt.title("Transposed")
        plt.show()

    except Exception as e:
        # ! Safe error catch
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
