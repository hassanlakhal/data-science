import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name : str
    surname : str
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default='Eagle')
    id: str = field(init=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = generate_id()
