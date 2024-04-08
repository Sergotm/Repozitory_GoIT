def parse_input(user_input): # Тут мы парсим строку в нижний регистр
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return 'Enter the argument for the command'
        except IndexError:
            return 'Enter the argument for the command'

    return inner


@input_error
def add_contact(args, contacts): # Тут мы додаем номер телефона
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error   
def change_contact(args, contacts): # Тут мы меняем старый номер на новый
    name, phone = args
    contacts[name] = phone
    return "Contact added replace."

@input_error
def show_phone(args, contacts): # Тут мы выводим номер указаного человека по ключу
    name = args[0]
    return name, contacts[name]

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
