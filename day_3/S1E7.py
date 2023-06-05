from S1E9 import Character

class Baratheon(Character):
    """Derived class representing a Baratheon character."""
    
    def __init__(self, first_name, family_name = "Baratheon", eyes = "brown", hairs = "dark"):
        super().__init__(first_name = first_name, is_alive = True)
        self.family_name = family_name 
        self.eyes = eyes
        self.hairs = hairs
    
    def die(self):
        """Method to change the health state of the Baratheon character to False."""
        self.is_alive = False
    
    def __str__(self):
        """String representation of the Baratheon character."""
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}, Alive: {self.is_alive}"
    
    def __repr__(self):
        """String representation of the Baratheon character."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
class Lannister(Character):
    """Derived class representing a Lannister character."""
    def __init__(self, first_name, is_alive = True,family_name = "Lannister", eyes = "blue", hairs = "light"):
        super().__init__(first_name = first_name, is_alive= is_alive)
        self.family_name = family_name 
        self.eyes = eyes
        self.hairs = hairs
            
    def die(self):
        """Method to change the health state of the Lannister character to False."""
        self.is_alive = False
    
    def __str__(self):
        """String representation of the Lannister character."""
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}, Alive: {self.is_alive}"
        
    def __repr__(self):
        """String representation of the Lannister character."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)