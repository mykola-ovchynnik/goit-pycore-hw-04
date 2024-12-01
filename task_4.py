def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) <= 1:
        return "Invalid number of arguments"

    name, phone = args

    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    if len(args) <= 1:
        return "Invalid number of arguments"

    name, new_phone_number = args

    if name not in contacts:
        return "Contact does not exist."

    contacts[name] = new_phone_number
    return "Contact updated."


def delete_contact(args, contacts):
    if len(args) < 1:
        return "Invalid number of arguments"

    name = args[0]

    if name not in contacts:
        return "Contact does not exist."

    del contacts[name]
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
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break

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
            case "exit" | "close":
                print("Good bye!")
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
