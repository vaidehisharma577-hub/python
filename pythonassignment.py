# mini_library.py
# Mini Library Management System
# Author: Your Name
# Date: 23 Nov 2025

class Book:
    def _init_(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        return f"{self.title:<30} {self.author:<20} {self.isbn:<15} {self.status:<10}"


# List to store books
library = []


# Task 2: Add Book
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN Number: ")
    status = input("Enter Status (Available/Issued): ")

    book = Book(title, author, isbn, status)
    library.append(book)
    print("\nBook added successfully!")


# Task 2: Search Book
def search_book():
    key = input("Enter Book Title or ISBN to search: ")
    found = False
    for book in library:
        if book.title.lower() == key.lower() or book.isbn == key:
            print("\nBook Found:")
            print(book.display())
            found = True
    if not found:
        print("Book not found!")


# Task 2: Remove Book
def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    for book in library:
        if book.isbn == isbn:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")
 

# Task 3: Save Records to File
def save_records():
    try:
        with open("library.txt", "w") as file:
            for book in library:
                file.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")
        print("Records saved to library.txt successfully!")
    except Exception as e:
        print("Error saving file:", e)


# Task 4: Load Records
def load_records():
    try:
        with open("library.txt", "r") as file:
            library.clear()
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    title, author, isbn, status = data
                    library.append(Book(title, author, isbn, status))
        print("Records loaded successfully from library.txt!")
    except FileNotFoundError:
        print("library.txt not found!")
    except Exception as e:
        print("Error loading file:", e)


# Task 5: Display All Books
def display_books():
    if not library:
        print("No books available!")
        return
    print("\n{:<30} {:<20} {:<15} {:<10}".format("Title", "Author", "ISBN", "Status"))
    print("-" * 80)
    for book in library:
        print(book.display())


# Task 6: Menu-driven Program
def menu():
    while True:
        print("\n===== MINI LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Remove Book")
        print("4. Display All Books")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            save_records()
        elif choice == "6":
            load_records()
        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")


# Run menu
menu()