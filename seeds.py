from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Chuck", "Palahniuk")
author_repository.save(author_1)
author_2 = Author("Patrick", "Ness")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("Fight Club", author_1, "Sci-fi", 1996)
book_repository.save(book_1)
book_2 = Book("Invisible Monsters", author_1, "Satire", 1999)
book_repository.save(book_2)
