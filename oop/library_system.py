class Book:
    id = 0 #unique class variable
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    id = 1 #unique class variable
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    def __repr__(self):
        return f"title = {self.title}, author = {self.author}, file_size = {self.file_size}"
    
class PrintBook(Book):
    id = 2 #unique class variable
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = [] #Bookshelf
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            '''Use if statements to track the class variable "id" which will enable --
            printing the books stored in #bookshelf by their respective classes'''
            print(book)
            # if  book.id == 2:
            #     print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            # elif book.id == 1:
            #     print(f"Ebook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            # elif book.id == 0:
            #     print(f"Book: {book.title} by {book.author}")