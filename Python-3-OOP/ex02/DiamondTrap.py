from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the false King Joffrey with diamond inheritance."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize King character defaulting to Baratheon heritage."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str) -> None:
        """Set eye color property."""
        self.__dict__["eyes"] = eyes

    def get_eyes(self) -> str:
        """Get eye color property."""
        return self.__dict__["eyes"]

    def set_hairs(self, hairs: str) -> None:
        """Set hair color property."""
        self.__dict__["hairs"] = hairs

    def get_hairs(self) -> str:
        """Get hair color property."""
        return self.__dict__["hairs"]

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)
