from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class LeafletFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:300]


class BookFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)
        return formatted_book


b = Book("A really good book!")
p = Printer()
print(p.get_book(b, BookFormatter()))
