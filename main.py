import camelcase

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
      
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully to the library.")
   
  def display_books(self):
    
        for book in self.books:
            print( f"Title: {book.title}, Author: {book.author}, "
                   f"ID: {book.id_number}, Category: {book.category}, "
                   f"Price: {book.get_price()} PLN" )
            
class Book:
    def __init__(self, title, author, id_number, category, price):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.category = category
        self.__price = price
        self.camel = camelcase.Camelcase()
        
  def get_price(self):
      return self.__price

  def get_camel_case_title(self):
      return self.camel.hump(self.title)
      
library = Library("Pałac Kultury Library", "Zlote Tarasy")
book1 = Book("The Tempest", "William Shakespeare", "1", "Classic", 120)
book2 = Book("The Farm", "George Orwell", "2", "Fiction", 150)
book3 = Book("Born a Crime", "Trevor Noah", "3", "Biography", 110)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
    
