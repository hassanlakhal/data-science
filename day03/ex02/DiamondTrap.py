from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
    
    def __init__(self, first_name):
        super().__init__(first_name)

    
    def set_eyes(self,eyes):
        self.eyes = eyes


    def set_hairs(self, hairs):
        self.hairs = hairs
    

    def get_eyes(self):
        return getattr(self, 'eyes', None)


    def get_hairs(self):
        return getattr(self, 'hairs', None)
    
    