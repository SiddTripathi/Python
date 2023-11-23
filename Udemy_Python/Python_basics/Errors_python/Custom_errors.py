#Custom errors are errors which are customized by you. However, they are extension of ValueError class so dont forget to create a Custom Error class before raising error. Like below

class PageReadError(ValueError):
    pass


class Book:
    def __init__(self,name: str, total_pages: int):
        self.name = name
        self.total_pages = total_pages
        self.pages_read = 0
    def __repr__(self):
        return f"<Book {self.name}, read {self.pages_read} pages out of {self.total_pages} pages"
    def read(self, pages:int):
        if self.pages_read + pages > self.total_pages:
            raise PageReadError (f"You cannot read {self.pages_read+pages} pages in a Book of {self.total_pages} pages")
        self.pages_read +=pages
        print(f"You have read {self.pages_read} pages out of {self.total_pages} pages")


book1 = Book("Harry Potter", 345)
book2 =  Book("Python 101",400)
try:
    book1.read(345)
    book2.read(404)
except PageReadError as e:
    print(e)
else:
    print("Done")
finally:
    print("Good Bye")
    