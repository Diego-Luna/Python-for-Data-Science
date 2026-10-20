from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon character with default traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Change the health state of character to dead."""
        # * Set character is_alive status to False
        self.is_alive = False

    def __str__(self) -> str:
        """Return string representation of Baratheon vector traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return official representation of Baratheon vector traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Lannister character with default traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Change the health state of character to dead."""
        # * Set character is_alive status to False
        self.is_alive = False

    def __str__(self) -> str:
        """Return string representation of Lannister vector traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return official representation of Lannister vector traits."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(
        cls, first_name: str, is_alive: bool = True
    ) -> "Lannister":
        """Create a new Lannister character instance."""
        # * Return a newly instantiated Lannister object
        return cls(first_name, is_alive)
