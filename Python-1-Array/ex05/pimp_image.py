import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    # * Allowed operators: =, +, -, *
    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("Invert")
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red color component of the image received."""
    # * Allowed operators: =, *
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    plt.imshow(red)
    plt.title("Red")
    plt.show()
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green color component of the image received."""
    # * Allowed operators: =, -
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    plt.imshow(green)
    plt.title("Green")
    plt.show()
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue color component of the image received."""
    # * Allowed operators: =
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.title("Blue")
    plt.show()
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image received to grayscale."""
    # * Allowed operators: =, /
    grey = array.copy()
    grey[:, :, 0] = array[:, :, 1] / 1
    grey[:, :, 2] = array[:, :, 1] / 1
    plt.imshow(grey)
    plt.title("Grey")
    plt.show()
    return grey
