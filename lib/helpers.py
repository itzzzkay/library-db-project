from models.book import Book
from models.member import Member
from models.borrowing import Borrowing

def exit_program():
    print("Goodbye!")
    exit()

from models.book import Book
from models.author import Author

def add_book():
    name = input("Enter book title: ")
    author_name = input("Enter author name: ")

    author = Author.find_by_name(author_name)
    if not author:
        author = Author(name=author_name)
        author.save()

    book = Book(name=name, author_id=author.id)
    book.save()
    print(f"Book '{name}' by {author_name} added successfully.")


def list_books():
    print("All Books:")
    books = Book.all()
    if not books:
        print("No books in the library.")
    for book in books:
        print(book)

def add_member():
    name = input("Enter member name: ")
    member = Member(name=name)
    member.save()
    print(f"Member '{member.name}' added successfully!")

def list_members():
    print("All Members:")
    members = Member.all()
    if not members:
        print("No members found.")
    for member in members:
        print(member)

def borrow_book():
    member_name = input("Member name: ")
    book_name = input("Book name: ")

    member = Member.find_by_name(member_name)
    book = Book.find_by_name(book_name)

    if member and book:
        Borrowing.borrow(book.id, member.id)
        print(f"{book.name} borrowed by {member.name}")
    else:
        print("Member or Book not found in the database.")

def list_borrowed():
    print("Borrowed Books:")
    borrowed = Borrowing.borrowed_books()
    if not borrowed:
        print("No books currently borrowed.")
    for book_name, member_name in borrowed:
        print(f"{book_name} borrowed by {member_name}")
