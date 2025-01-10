from book import Book
from library import Library

library = Library("Centrum Library", "Zlote Tarasy")
book1 = Book("The Tempest", "William Shakespeare", "1", "Classic", 120)
book2 = Book("The Farm", "Joanne Ramos", "2", "Fiction", 150)
book3 = Book("Born a Crime", "Trevor Noah", "3", "Biography", 110)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()