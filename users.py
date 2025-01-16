from person import Person

class User(Person):
    def __init__(self,fullname, age, user_id):
        super().__init__(fullname, age, user_id)
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"User: {self.name}, UserID: {self.user_id}, Borrowed Books: {len(self.borrowed_books)}"