# Contact Book in Python

contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("\nContact found:")
        print(f"Name   : {name}")
        print(f"Phone  : {contacts[name]['phone']}")
        print(f"Email  : {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print("Contact not found.")

def edit_contact():
    name = input("Enter name to edit: ")
    if name in contacts:
        print("Enter new details:")
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    print("\n=== All Contacts ===")
    for name, info in contacts.items():
        print(f"\nName   : {name}")
        print(f"Phone  : {info['phone']}")
        print(f"Email  : {info['email']}")
        print(f"Address: {info['address']}")

def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
