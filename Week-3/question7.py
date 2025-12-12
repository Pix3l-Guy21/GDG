#No7
class Library:

    def __init__(self, books: list):
        self.books = books
    
    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        return f'list of books in the library: {self.books}'

l1 = Library(["The Jungle Book", "Lord of the rings", "The Hobbit", "1984"])
l1.add_book('Harry Potter')
print(l1.show_books())