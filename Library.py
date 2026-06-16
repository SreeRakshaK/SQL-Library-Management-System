import sqlite3

def initialize_database():
    """Connects to a database file and creates a clean structural table."""
    connection = sqlite3.connect("library_db.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_book(title, author):
    """Inserts a new book record securely into our SQL database."""
    connection = sqlite3.connect("library_db.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, status) VALUES (?, ?, ?)",
        (title, author, "Available")
    )
    connection.commit()
    connection.close()
    print(f"\n✅ Added '{title}' to the catalog!")

def view_all_books():
    """Fetches every row from the SQL table and prints it clearly."""
    connection = sqlite3.connect("library_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author, status FROM books")
    all_rows = cursor.fetchall()
    connection.close()
    
    if not all_rows:
        print("\nThe library database is empty.")
        return
        
    print("\n================ LIBRARY INVENTORY ================")
    for row in all_rows:
        print(f"ID: {row[0]:<3} | Title: {row[1]:<22} | Author: {row[2]:<15} | [{row[3]}]")
    print("===================================================\n")

def borrow_book(book_id):
    """
    NEW DATABASE FUNCTION: Updates the status of a book to 'Checked Out' 
    using its unique database ID number.
    """
    connection = sqlite3.connect("library_db.db")
    cursor = connection.cursor()
    
    # Run an SQL UPDATE query targeting a specific ID row
    cursor.execute(
        "UPDATE books SET status = ? WHERE id = ? AND status = ?",
        ("Checked Out", book_id, "Available")
    )
    
    # cursor.rowcount tells us if SQL actually found and updated a row
    if cursor.rowcount > 0:
        print(f"\n📖 Success! Book ID {book_id} has been checked out.")
    else:
        print(f"\n❌ Error: Book ID {book_id} is either invalid or already checked out.")
        
    connection.commit()
    connection.close()

def return_book(book_id):
    """
    NEW DATABASE FUNCTION: Updates the status of a book back to 'Available'.
    """
    connection = sqlite3.connect("library_db.db")
    cursor = connection.cursor()
    
    cursor.execute(
        "UPDATE books SET status = ? WHERE id = ? AND status = ?",
        ("Available", book_id, "Checked Out")
    )
    
    if cursor.rowcount > 0:
        print(f"\n↩️ Success! Book ID {book_id} has been returned to the shelf.")
    else:
        print(f"\n❌ Error: Book ID {book_id} is either invalid or already available.")
        
    connection.commit()
    connection.close()

def main_menu():
    """The interactive loop that powers our terminal menu."""
    initialize_database()
    
    while True:
        print("\n*** PRODUCTION DB LIBRARY MANAGEMENT SYSTEM ***")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Check-Out a Book (Borrow)")
        print("4. Check-In a Book (Return)")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            if title and author:
                add_book(title, author)
            else:
                print("\n❌ Error: Fields cannot be blank.")
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            view_all_books() # Show list first so user can see IDs
            book_id = input("Enter the ID of the book to borrow: ").strip()
            if book_id.isdigit():
                borrow_book(int(book_id))
            else:
                print("\n❌ Error: Please enter a valid numerical ID.")
        elif choice == "4":
            book_id = input("Enter the ID of the book to return: ").strip()
            if book_id.isdigit():
                return_book(int(book_id))
            else:
                print("\n❌ Error: Please enter a valid numerical ID.")
        elif choice == "5":
            print("\nExiting Database... Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()