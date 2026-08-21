contacts = []


def show_menu():
    print("\n" + "=" * 35)
    print("      CONTACT DIRECTORY")
    print("=" * 35) # replciate * 35 times

    print("1. Add a contact")
    print("2. Display all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")


def add_contact():
    name = input("Enter the name : " )
    phone_number = input("Enter the phone number : " )
    email = input("Enter the email : " )


    contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone_number,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully !")




while True:
    show_menu()

    choice = input("type your choice in here: ")

    if choice == "1":
        print("Add a contact")

    elif choice == "2":
        print("Display all contact")

    elif choice == "3":
        print("Search contact")

    elif choice == "4":
        print("Update contact")

    elif choice == "5":
        print("Delete contact")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")