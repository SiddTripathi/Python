class Book:
    TYPE = ('hardcover','paperback')
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"Book {self.book_type},{self.name},{self.weight}"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPE[0], page_weight+100)
    @classmethod
    def paperbook(cls, name, page_weight):
        return Book(name, Book.TYPE[1], page_weight)
    @staticmethod
    def example():
        return "Hello This is Static method does not require args"



book = Book.hardcover('Harry Potter',1500)
book2 = Book.paperbook('Lord Rings',1200)
print(Book.hardcover('Harry',1200))
print(Book.example())
print(book)
print(book2)