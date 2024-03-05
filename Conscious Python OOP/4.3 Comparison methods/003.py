class Books:
    def __init__(self, book_name, book_page):
        self.book_name = book_name
        self.book_page = book_page

    def __le__(self, other):
        if isinstance(other, Books):
            return self.book_page <= other.book_page

    def __ge__(self, other):
        if isinstance(other, Books):
            return self.book_page >= other.book_page


book1 = Books('Война и мир', 1360)
book2 = Books('Собака Баскервилей', 112)
book3 = Books('Скотный двор', 112)

print(book1 >= book2)
print(book1 >= book3)
print(book2 <= book3)
