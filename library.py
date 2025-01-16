from borrow import Borrowing
from datetime import date
class Library:
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, "
                  f"ID: {book.id_number}, Category: {book.category}, "
                  f"Price: {book.get_price()}pln")
   
    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"User: {self.name}, UserID: {self.user_id}, Borrowed Books: {len(self.borrowed_books)}"              
    
    
    def __init__(self):
        self.borrowings = []

    def borrow_book(self, book, user_id, librarian_id):
        borrow_date = date.today()
        return_date = borrow_date.replace(day=borrow_date.day + 14)  # Assuming a 2-week borrow period
        borrowing = Borrowing(user_id, book, borrow_date, return_date, librarian_id)
        self.borrowings.append(borrowing)

    def return_book(self, book, user_id, librarian_id):
        for borrowing in self.borrowings:
            if borrowing.book == book and borrowing.user_id == user_id:
                borrowing.return_date = date.today()
                print(f"Book {book} returned successfully!")
                return
        print("Borrowing record not found.")