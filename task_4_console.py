import sys
import json
from task_4 import add_contact, change_contact, delete_contact, show_all, show_phone

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
            result = add_contact(args, contacts)
            save_contacts(contacts)
            print(result)
        case "change":
            result = change_contact(args, contacts)
            save_contacts(contacts)
            print(result)
        case "delete":
            result = delete_contact(args, contacts)
            save_contacts(contacts)
            print(result)
        case "phone":
            print(show_phone(args, contacts))
        case "all":
            print(show_all(contacts))
        case "exit" | "close":
            print("Good bye!")
        case _:
            print("Invalid command")


if __name__ == "__main__":
    main()
