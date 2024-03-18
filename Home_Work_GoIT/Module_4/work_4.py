def parse_input(user_input): # Тут мы парсим строку в нижний регистр
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): # Тут мы додаем номер телефона
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return f'Not name and number argument'
    
def change_contact(args, contacts): # Тут мы меняем старый номер на новый
    name, phone = args
    contacts[name] = phone
    return "Contact added replace."

def show_phone(args, contacts): # Тут мы выводим номер указаного человека по ключу
    try:
        name = args[0]
        return name, contacts[name]
    except KeyError:
        return(f"Not it's Username")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
