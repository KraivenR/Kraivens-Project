from library import Library
from users import User
from librarian import Librarian


user1 = User("Kraiven", 20, 651743)
librarian1 = Librarian("Roksana", 47, 347154)

library = Library()

library.borrow_book("The tempest", user1.user_id, librarian1.user_id)

library.return_book(" Animal farm", user1.user_id, librarian1.user_id)
