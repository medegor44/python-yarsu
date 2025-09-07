class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}")


class LibraryUser:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title}.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed book: {book.title}")
        else:
            print(f"Book {book.title} not found in the library.")

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book {title} not found.")
        return None


# Пример использования
library = Library()
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

library.add_book(book1)
library.add_book(book2)

user = LibraryUser("Alice", 1)
user.borrow_book(book1)
user.return_book(book1)