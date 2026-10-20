class calculator:
    """Calculator providing static methods for 2-vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        # * Sum element-wise products
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise sum of two vectors."""
        # * Compute element-wise addition as floats
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise subtraction of two vectors."""
        # * Compute element-wise subtraction as floats
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
