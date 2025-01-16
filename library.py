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
                  