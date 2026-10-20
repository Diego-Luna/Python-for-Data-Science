from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a Game of Thrones character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize character with first name and living status."""
        # * Store character identity and status
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Change the health state of character to dead."""
        pass


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Change the health state of character to dead."""
        # * Set character is_alive status to False
        self.is_alive = False
