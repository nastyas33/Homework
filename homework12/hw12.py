from typing import NamedTuple


class UserAnnotation(NamedTuple):
    email: str
    age: int

class User:
    def __init__(self, name: str, surname: str, age: int, country: str, gender: str, profession: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def generate_birth_year(self):
        return f"Birth year of {self.name} {self.surname} is {2022 - self.age}"

    def generate_email(self):
        return f"Email of {self.name} {self.surname} is {self.name}.{self.surname}@gmail.com"

def result(self):
    result_list = [us.profession for us in USERS if us.profession == "Teacher"]
    return f"User profession is {self.profession}"

user1 = User(name="Kate", surname="Smith", age=30, country="Poland", gender="female", profession="Lawyer")
user2 = User(name="Adam", surname="Paul", age=46, country="USA", gender="male", profession="Driver")
user3 = User(name="Dan", surname="Adams", age=39, country="Canada", gender="male", profession="Doctor")
user4 = User(name="Christian", surname="Gatsbi", age=46, country="China", gender="male", profession="Policeman")
user5 = User(name="Elizabeth", surname="Brown", age=33, country="Portugal", gender="female", profession="Teacher")

USERS = [user1, user2, user3, user4, user5]

print(result(self=user1))
