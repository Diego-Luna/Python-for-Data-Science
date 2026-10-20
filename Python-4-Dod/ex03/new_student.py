from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    """Generate a random 15-character string ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student record."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Compute student login based on name and surname."""
        # * Create login combining first initial and full surname
        self.login = self.name[:1] + self.surname
