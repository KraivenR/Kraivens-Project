from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod

    def display_details(self):
        pass
class Student(Person):
    def __init__(self,name, surname, age, user_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.user_id = user_id

    def display_details(self):
        print(f"student full name is {self.name},he is {self.age} years old an his student ID is {self.user_id}")

people = [Student("Kraiven","Ribeiro", 20, "34714")]

for person in people:
    print(person.display_details())