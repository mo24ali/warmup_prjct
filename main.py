FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 4:
                    continue

                contact_id, name, phone, email = parts
                try:
                    contact_id = int(contact_id)
                except ValueError:
                    continue

                contacts.append({
                    "id": contact_id,
                    "name": name,
                    "phone": phone,
                    "email": email
                })
    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        for contact in contacts:
            f.write(f"{contact['id']},{contact['name']},{contact['phone']},{contact['email']}\n")


def read_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid number. Please enter a whole number.")


def show_menu():
    print("\n" + "=" * 35)
    print("      CONTACT DIRECTORY")
    print("=" * 35)

    print("1. Add a contact")
    print("2. Display all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")


def add_contact(contacts):
    name = input("Enter the name : ")
    phone_number = input("Enter the phone number : ")
    email = input("Enter the email : ")

    contact = {
        "id": contacts[-1]["id"] + 1 if contacts else 1,
        "name": name,
        "phone": phone_number,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully !")


def display_all_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    for contact in contacts:
        print(f"\nID: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 30)


def search_contact(contacts):
    id_to_search = read_int("Enter the id to be found : ")
    found = False

    for contact in contacts:
        if contact["id"] == id_to_search:
            print(f"\nID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 30)
            found = True
            break

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    id_to_update = read_int("Enter the id of the contact to update : ")

    for contact in contacts:
        if contact["id"] == id_to_update:
            print("Press Enter to keep the current value.")

            new_name = input(f"Enter the name ({contact['name']}) : ")
            new_phone = input(f"Enter the phone number ({contact['phone']}) : ")
            new_email = input(f"Enter the email ({contact['email']}) : ")

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)
            print("Contact updated successfully !")
            return

    print("Contact not found.")


def delete_contact(contacts):
    id_to_delete = read_int("Enter the id of the contact to delete : ")

    for contact in contacts:
        if contact["id"] == id_to_delete:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully !")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("type your choice in here: ")

        if choice == "1":
            print("Add a contact")
            add_contact(contacts)

        elif choice == "2":
            print("Display all contact")
            display_all_contacts(contacts)

        elif choice == "3":
            print("Search contact")
            search_contact(contacts)

        elif choice == "4":
            print("Update contact")
            update_contact(contacts)

        elif choice == "5":
            print("Delete contact")
            delete_contact(contacts)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()