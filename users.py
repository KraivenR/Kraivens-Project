from person import Person

class User(Person):
    def __init__(self,fullname, age, user_id):
        super().__init__(fullname, age, user_id)
    
        self.borrowed_books = []

   