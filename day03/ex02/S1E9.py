from abc import ABC, abstractmethod


class Character(ABC):
    """Base abstract character class"""

    def __init__(self, first_name, is_alive=True):
        """Initializes the character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        pass

class Stark(Character):
    """Stark family character"""

    def die(self):
        """change status of alive to False"""
        self.is_alive = False

