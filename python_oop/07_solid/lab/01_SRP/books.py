from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def find_book(self, title) -> str or Book:
        try:
            book = next(filter(lambda b: b.title == title, self.books))
        except StopIteration:
            return "Sorry, there is no such book in the library"

        return book

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        result = self.find_book(book)
        if isinstance(result, Book):
            self.books.remove(result)

    def __str__(self):
        result = [f"{len(self.books)} books in the library:"]
        result += [str(b) for b in self.books]
        return f"\n".join(result)


library = Library()
for num in range(1, 6):
    b = Book(f"Title {num}", f"Author {num}")
    library.add_book(b)

library.remove_book("Title 5")
print(library)
