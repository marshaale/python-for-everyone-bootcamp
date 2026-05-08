from dataclasses import dataclass

@dataclass
class Book:
    title:str
    author:str

class Shelf:
    def __init__(self):
        self.books = []
    
    def add(self,book):
        self.books.append(book)
    
    def titles(self):
        return [book.title for book in self.books]


book1 = Book("Do not say","Liam Delap")
book2 = Book("Skye is the limit","Abdalla Hasasi")

shelf = Shelf()
shelf.add(book1)
shelf.add(book2)
print(shelf.titles())