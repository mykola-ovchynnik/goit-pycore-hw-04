import sys
import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)


def parse_input(args):
    cmd = args[0].strip().lower()
    return cmd, args[1:]


def add_contact(args, contacts):
    if len(args) <= 1:
        return "Invalid number of arguments"

    name, phone = args

    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone
    save_contacts(contacts)
    return "Contact added."


def change_contact(args, contacts):
    if len(args) <= 1:
        return "Invalid number of arguments"

    name, new_phone_number = args

    if name not in contacts:
        return "Contact does not exist."

    contacts[name] = new_phone_number
    save_contacts(contacts)
    return "Contact updated."


def delete_contact(args, contacts):
    if len(args) < 1:
        return "Invalid number of arguments"

    name = args[0]

    if name not in contacts:
        return "Contact does not exist."

    del contacts[name]
    save_contacts(contacts)
    return "Contact deleted."


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    return contacts


def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid number of arguments"

    name = args[0]

    if name not in contacts:
        return "Contact does not exist."

    return contacts[name]


def main():
    contacts = load_contacts()

    if len(sys.argv) < 2:
        print("No command provided.")
        return

    command, args = parse_input(sys.argv[1:])

    match command:
        case "hello":
            print("How can I help you?")
        case "add":
            print(add_contact(args, contacts))
        case "change":
            print(change_contact(args, contacts))
        case "delete":
            print(delete_contact(args, contacts))
        case "phone":
            print(show_phone(args, contacts))
        case "all":
            print(show_all(contacts))
        case "exit":
            print("Good bye!")
        case _:
            print("Invalid command")


if __name__ == "__main__":
    main()
