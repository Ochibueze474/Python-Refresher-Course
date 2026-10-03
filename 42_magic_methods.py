# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python's built-in operations
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
            return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages   

    def __gt__(self, other):
        return self.num_pages > other.num_pages 

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages in total"

    def __contains__(self, keyword):
         return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
         if key == "title":
             return self.title
         elif key == "author":
             return self.author
         elif key == "num_pages":
             return self.num_pages
         else:
             return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and The Wardrobe", "C.S. Lewis", 172)

# Example of __str__ magic method
print(book1)
print(book2)
print(book3)
print()

# Example of __eq__ magic method
print(book1 == book2)  # False
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)   
print(book1 == book4)  # True
print()

# Example of __lt__ magic method
print(book1 < book2)  # False
print(book3 < book2)  # True
print()

# Example of __gt__ magic method
print(book1 > book2)  # True    
print(book3 > book2)  # False
print()

# Example of __add__ magic method
print(book1 + book2)

# Example of __contains__ magic method
print("Lion" in book3)  # True
print("Hobbit" in book2)  # False
print("J.K. Rowling" in book2)  # True
print("C.S. Lewis" in book1)  # False
print()

# Example of __getitem__ magic method
print(book1["title"])  # The Hobbit
print(book2["author"])  # J.K. Rowling
print(book3["num_pages"])  # 172
print(book1["publisher"])  # Key 'publisher' was not found in Book object