from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive = True, family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs
        Baratheon.__init__(self, first_name, family_name, eyes, hairs)
        Lannister.__init__(self, family_name, eyes, hairs)
        
    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    def set_eyes(self, eyes):
        self.eyes = eyes
    
    def get_eyes(self):
        return self.eyes
    
    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_hairs(self):
        return self.hairs
    