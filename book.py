class Book:

    def __init__(self, title, author, id_number, category, price):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.category = category
        self.__price = price

    def get_price(self):
        return self.__price