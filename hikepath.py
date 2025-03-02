import os


def main():
    print("Welcome to HikePath!")
    while True:
        # Command line variables
        user_input = input("> ")
        parts = user_input.split(" ", 1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        # Main commands
        if command in ("ls", "dir"):
            try:
                print(os.listdir(os.getcwd()))
            except Exception as e:
                print(f"An error occurred: {e}")

        elif command == "help":
            print("Available commands:")
            print("  ls (or dir)    - List files and folders in current directory")
            print("  cd <path>      - Change to directory <path>")
            print("  mkdir <name>   - Create a new directory <name>")
            print("  rmdir <name>   - Remove directory <name>")
            print("  exit           - Exit the program")
            print("  help           - Show this help message")

        elif command == "cd":
            if argument == "":
                print("An error occurred: Argument is missing")
            else:
                try:
                    os.chdir(argument)
                    print(f"Current path: {os.getcwd()}")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
        elif command == "mkdir":
            if argument == "":
                print("An error occurred: Argument is missing")
            else:
                try:
                    os.mkdir(argument)
                    print(f"Directory '{argument}' created")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif command == "rmdir":
            if argument == "":
                print("An error occurred: Argument is missing")
            else:
                try:
                    os.rmdir(argument)
                    print(f"Directory '{argument}' removed")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif command == "exit":
            print("Bye!")
            break

        else:
            print("Unknown command")


main()
