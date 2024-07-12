class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_checked_out = False

    def check_out_book(self, book_title):
        #checks if the book title is same as book_title, if yes set _is_checked_out as true
        if self._title == book_title:
            self._is_checked_out = True
            return True
        return False

    def return_book(self, book_title):
        #checks if the book title is same as book_title, if yes set _is_checked_out as false
        if self._title == book_title:
            self._is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def list_available_books(self):
    #Create a new list to filter books that are still available(_is_checked_out = False)
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books: #Iterate through the new list of books in the library
            print(f"{book._title} by {book._author}")

    def check_out_book(self, book_title):
        for book in self._books:
            if book.check_out_book(book_title):
                return
    def return_book(self, book_title):
        for book in self._books:
            if book.return_book(book_title):
                return