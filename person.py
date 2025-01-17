from abc import ABC,abstractmethod

class Person(ABC):

    def __init__(self, fullname, age, user_id):
        self.fullname = fullname
        self.age = age 
        self.user_id = user_id
@abstractmethod
def display_details(self): 
    return f"Name: {self.fullname}, Age: {self.age}"