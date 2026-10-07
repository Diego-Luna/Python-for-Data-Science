import os
from PIL import Image
import numpy as np


def ft_load(path: str, verbose: bool = True) -> np.ndarray | None:
    """Load an image, print its shape, and return RGB pixel array."""
    try:
        # ! Path validations
        if not isinstance(path, str):
            raise AssertionError("Path must be a string.")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: '{path}'")

        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("Supported formats are JPG and JPEG.")

        # * Convert image to RGB numpy array
        with Image.open(path) as img:
            arr = np.array(img.convert("RGB"))
            if verbose:
                print(f"The shape of image is: {arr.shape}")
            return arr

    except Exception as e:
        # ! Print clear error message without unhandled crashes
        print(f"Error: {e}")
        return None
