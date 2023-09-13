class BookShelf:
    def __init__(self,*books):
       
        self.books = books
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"
    
class Books:
    def __init__(self,name):
       
        self.name =  name
    def __str__(self):
        return f"Book {self.name}"


book = Books("Harry Potter")
book2 = Books("Python 101")




shelf =  BookShelf(book,book2)
print(shelf)
print(*shelf.books)
