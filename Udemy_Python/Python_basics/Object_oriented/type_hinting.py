class ClassTest:
    def instance_mthd(self):
        print(f"Called instance method of {self}")
    

    @classmethod
    def class_mthd(cls):
        print(f"Called class method of {cls}")
    
    @staticmethod
    def static_mthd():
        print("Called Static method")


test = ClassTest()
test.instance_mthd()
test.static_mthd()
ClassTest.class_mthd()              #For Instance method, need to create object. But for class and static method, no need to create object. Though, Object can also access these methods 
ClassTest.static_mthd()
ClassTest.instance_mthd(test)


#Example class method
#Now in this book class, one can pass any book type(comic, action etc.) unless you make it clear somehow that book type can be hard cover or paper back nothing else. For this use class method. See how
#added data type for Type hinting in arguments of methods
class Book:
    BOOK_TYPE = ("hardcover","paperback")
    def __init__(self,name: str,book_type: str,weight: int):
        self.name =name
        self.book_type=book_type
        self.weight = weight
    def __str__(self) ->str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}"
    @classmethod
    def hardcover(cls,name: str,page_weight: int):
        return cls(name, cls.BOOK_TYPE[0],page_weight+100)
    @classmethod
    def paperback(cls,name: str,page_weight: int):
        return cls(name, cls.BOOK_TYPE[1],page_weight)
    
    @staticmethod
    def testing(book):
        return f" static method prints {book.name}"
    

book =  Book("Harry Potter","hardcover",200)

print(Book.testing(book))


print(book.name)