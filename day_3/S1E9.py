from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class representing a character."""
    
    def __init__(self, first_name, is_alive=True):
        """Constructor for the Character class."""
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        """Method to change the health state of the character to False."""
        pass


class Stark(Character):
    """Derived class representing a Stark character."""
    
    def die(self):
        """Method to change the health state of the Stark character to False."""
        self.is_alive = False