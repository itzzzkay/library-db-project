from models.book import Book
from models.author import Author
from models.member import Member
from models.borrowing import Borrowing

Book.create_table()
Author.create_table()
Member.create_table()
Borrowing.create_table()

author = Author(name="J.K. Rowling")
author.save()

book = Book(name="Harry Potter", author=author.name)
book.save()

found = Book.find_by_name("Harry Potter")
print("Found:", found)

member = Member(name="Kyle")
member.save()
