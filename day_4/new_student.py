import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

# With dataclass decorator, you can automatically
# generate common boilerplate methods for your class,
# such as __init__(), __repr__(), __eq__(),
@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(init=False)
    login_: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)
    
    # __post_init__() we can initiate attributes later
    def __post_init__(self):
        if not self.name or not self.surname:
            raise ValueError("Missing or invalid arguments when creating a Student object.")
        else:
            self.login_ = self.logi(self.name, self.surname)
            self.active = True
            self.login_ = self.logi(self.name, self.surname)
            self.id = generate_id()

    # Merge first letter of name in capital with surname in lowcase
    def logi(self, name, surname):
        first_letter_name = name[0].upper()
        lowercase_surname = surname.lower()
        return first_letter_name + lowercase_surname

    