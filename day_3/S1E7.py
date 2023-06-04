from S1E9 import Character

class Baratheon(Character):
    """Derived class representing a Baratheon character."""
    
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"
    
    def die(self):
        """Method to change the health state of the Baratheon character to False."""
        self.is_alive = False
    
    def __str__(self):
        """String representation of the Baratheon character."""
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}, Alive: {self.is_alive}"
    
    def __repr__(self):
        """String representation of the Baratheon character."""
        return f"Character: {self.first_name}"
    

class Lannister(Character):
    """Derived class representing a Lannister character."""
    def __init__(self, my_variable):
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
        """Method to change the health state of the Lannister character to False."""
        self.is_alive = False
    
    def __str__(self):
        """String representation of the Lannister character."""
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}, Alive: {self.is_alive}"
    
    def __repr__(self):
        """String representation of the Lannister character."""
        return f"Character: {self.first_name}"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)