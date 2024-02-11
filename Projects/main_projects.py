# 1.Simple Contact List
contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter contact phone number: ")
    contacts.append({"name": name, "phone_number": phone_number})
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")

def delete_contact():
    name = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print(f"Contact '{name}' not found.")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")





# 2.Mini Library
books = []

def add_book():
    name = input("Enter name of Book: ")
    about = input("Write about Book: ")
    books.append({"name": name, "description": about})
    print(f"Book '{name}' added successfully.")

def view_books():
    if not books:
        print("No Books available.")
    else:
        print("Books:")
        for book in books:
            print(f"Name: {book['name']}, Description: {book['description']}")

def delete_book():
    name = input("Enter book name to delete: ")
    for book in books:
        if book["name"] == name:
            books.remove(book)
            print(f"Book '{name}' deleted successfully.")
            return
    print(f"Book '{name}' not found.")

while True:
    print("\nOptions:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")




# 3.













