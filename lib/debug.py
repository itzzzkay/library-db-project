from models import CONN
from models.book import Book
from models.author import Author
from models.member import Member
from models.borrowing import Borrowing

Book.drop_table()

Author.create_table()
Book.create_table()
Member.create_table()
Borrowing.create_table()

authors = [
    Author(name="Rick Riordan"),
    Author(name="J.K. Rowling"),
    Author(name="Jane Austen")
]
for author in authors:
    author.save()

books = [
    Book(name="Percy Jackson: The Lightning Thief", author_id=authors[0].id),
    Book(name="Percy Jackson: The House of Hades", author_id=authors[0].id),
    Book(name="Harry Potter and the Sorcerer's Stone", author_id=authors[1].id),
    Book(name="Harry Potter and the Chamber of Secrets", author_id=authors[1].id),
    Book(name="Pride and Prejudice", author_id=authors[2].id),
    Book(name="Emma", author_id=authors[2].id)
]
for book in books:
    book.save()

members = [
    Member(name="Kyle"),
    Member(name="Yvonne"),
    Member(name="Bob")
]
for member in members:
    member.save()

Borrowing.borrow(books[0].id, members[0].id)  
Borrowing.borrow(books[1].id, members[0].id)  
Borrowing.borrow(books[2].id, members[1].id)  
Borrowing.borrow(books[5].id, members[1].id)  
Borrowing.borrow(books[4].id, members[2].id)  
Borrowing.borrow(books[3].id, members[2].id)

print(" Borrowed Books:")
borrowed = Borrowing.borrowed_books()
for book_title, member_name in borrowed:
    print(f"{book_title}  borrowed by {member_name}")



