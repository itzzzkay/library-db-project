from models.book import Book
from models.author import Author
from models.member import Member
from models.borrowing import Borrowing

def tables():
    Book.create_table()
    Author.create_table()
    Member.create_table()
    Borrowing.create_table()

from helpers import (
    exit_program,
    add_book,
    list_books,
    add_member,
    borrow_book,
    list_borrowed,
    list_members
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            add_member()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            list_borrowed
        elif choice == "6":
            list_members

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Add Member")
    print("4. Borrow Book")
    print("5. List Borrowed Books")
    print("6. List All Members")

def run():
    tables()


if __name__ == "__main__":
    main()