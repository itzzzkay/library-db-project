from models.book import Book
from models.member import Member
from models.borrowing import Borrowing

def exit_program():
    print("Goodbye!")
    exit()
    
def add_book():
    name = input("Book name: ")
    author = input("Author name: ")
    book = Book(name=name, author=author)
    book.save()
    print("Book Saved:)")

def list_books():
    books = Book.all()
    for book in books:
        print(book)

def add_member():
    name = input("Member name: ")
    member = Member(name=name)
    member.save()
    print("Member saved:)")

def borrow_book():
    member_name = input("Member name: ")
    book_name = input("Book name: ")
    
    member = Member.find_by_name(member_name)
    book = Book.find_by_name(book_name)

    if member and book:
        Borrowing.borrow(book.id, member.id)
        print(f"{book.name} borrowed by {member.name}")
    else:
        print(" Member or Book not present in database:(")

def list_borrowed():
    borrowed = Borrowing.borrowed_books()
    for book in borrowed:
        print(f"{book[0]} borrowed by {book[1]}")
    
def list_members():
    members = Member.all()
    for member in members:
        print(member)

