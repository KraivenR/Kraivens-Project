from person import Person

class Librarian(Person):
    def __init__(self, fullname, age, librarian_id):
         super().__init__(fullname, age)
         self.librarian_id = librarian_id