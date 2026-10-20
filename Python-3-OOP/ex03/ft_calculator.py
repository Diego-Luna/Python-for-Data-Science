class calculator:
    """Calculator for element-wise arithmetic of vector with scalar."""

    def __init__(self, vector: list[float]) -> None:
        """Initialize calculator with a vector of numbers."""
        # * Convert all items to float for consistent operations
        self.vector = [float(x) for x in vector]

    def __add__(self, object: float | int) -> None:
        """Add scalar to all vector elements in-place and print."""
        # * Add scalar to each element and store result
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object: float | int) -> None:
        """Multiply all vector elements by scalar in-place and print."""
        # * Multiply each element by scalar and store result
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object: float | int) -> None:
        """Subtract scalar from all vector elements in-place and print."""
        # * Subtract scalar from each element and store result
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object: float | int) -> None:
        """Divide all vector elements by scalar in-place and print."""
        # ! Guard against division by zero
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        # * Divide each element by scalar and store result
        self.vector = [x / object for x in self.vector]
        print(self.vector)
