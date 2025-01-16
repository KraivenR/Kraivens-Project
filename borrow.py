
class Borrowing:
    def __init__(self, user_id, book, borrow_date, return_date, librarian_id):
         self.user_id = user_id
         self.book = book
         self.borrow_date = borrow_date
         self.return_date = return_date
         self.librarian_id = librarian_id

    def __str__(self):
        return f"Book: {self.book}, Borrowed by: {self.user_id}, Borrowed on: {self.borrow_date}, Returned on: {self.return_date}"
    