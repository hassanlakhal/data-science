from S1E9 import Character

class Baratheon(Character):
    """Baratheon family character"""

    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Lannister family character"""

    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Lannister"
        self.eyes = "green"
        self.hairs = "blonde"

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(self, first_name):
        return Lannister(first_name)

