class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False #default attribute

    def check_out(self):
        #checks if the book title is same as book_title, if yes the state of _is_checked_out becomes true
        if not self._is_checked_out:
            self._is_checked_out = True
        return

    def return_book(self):
        #checks if the book title is same as book_title, if yes the state of _is_checked_out becomes false
        if self._is_checked_out:
            self._is_checked_out = False
        return

class Library:
    def __init__(self):
        self._books = [] #Book shelf

    def add_book(self, book):
        self._books.append(book)
    
    def list_available_books(self):
    #Create a new list to filter books that are still available(_is_checked_out = False)
        for book in self._books:
            if book._is_checked_out == False:
                available_books = [book]
                for book in available_books: #Iterate through the new list of books in the library
                    print(f"{book.title} by {book.author}")


    def check_out_book(self, book_title):
        #Iterate through the shelf (self._books)
        for book in self._books:
        #Runs every book in the shelf and cross reference the book_title with book titles in the #Book shelf and checks out using the check_out method in the class Book    
            if (book.title == book_title) and (not book._is_checked_out):
                book.check_out()
                return

    def return_book(self, book_title):
    #Runs every book in the shelf and cross reference the book_title value with book titles in the #Book shelf and returns them using the return_book method in the class Book 
        for book in self._books:
            if book.title == book_title and book._is_checked_out:
                book.return_book()
                return