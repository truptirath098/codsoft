#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number, email, address):
        self.contacts[name] = {'number': number, 'email': email, 'address': address}
        print(f"Contact '{name}' added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, query):
        found = False
        for name, contact_info in self.contacts.items():
            if query in name or query in contact_info['number'] or query in contact_info['email'] or query in contact_info['address']:
                print(f"Name: {name}")
                print(f"Number: {contact_info['number']}")
                print(f"Email: {contact_info['email']}")
                print(f"Address: {contact_info['address']}")
                found = True
        if not found:
            print(f"No contact found matching '{query}'.")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for name, contact_info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Number: {contact_info['number']}")
                print(f"Email: {contact_info['email']}")
                print(f"Address: {contact_info['address']}")
                print()

    def update_contact(self, name, new_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['number'] = new_number
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, number, email, address)
        elif choice == '2':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '3':
            query = input("Enter name, number, email, or address to search: ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Enter name to update: ")
            new_number = input("Enter new number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_number, new_email, new_address)
        elif choice == '5':
            contact_book.display_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

