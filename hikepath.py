import os
import shutil

def main():
    print("Welcome to HikePath!")
    history = []

    while True:
        # Command line variables
        user_input = input("> ")
        parts = user_input.split(" ", 2)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""
        argument_2 = parts[2] if len(parts) > 2 else ""

        if command != "history":
            history.append(user_input)

        # Main commands
        if command in ("ls", "dir"):
            try:
                print("\n".join(
                    f"📁 {item}" if os.path.isdir(item) else f"📄 {item}"
                    for item in os.listdir(os.getcwd())
                ))
            except Exception as e:
                print(f"An error occurred: {e}")

        elif command == "help":
            print('''  Available commands:
    ls (or dir)               - List files and folders in the current directory or at <path>
    cd <path>                 - Change to directory <path>
    mkdir <name>              - Create a new directory <name>
    rmdir <name> <argument>   - Remove directory <name>. Use '-r' for recursive removal.
    exit                      - Exit the program
    help                      - Show this help message
    history                   - Show the last 5 commands

  Note:
    - When using 'cd', if no path is specified, it defaults to the home directory.
    - Use 'rmdir' without '-r' for non-recursive deletion (only empty directories).
    - Errors may occur if a directory or file does not exist or if there are permission issues.''')

        elif command == "history":
            try:
                if not history:
                    print("Command history is empty")
                else:
                    print(*history[-5:], sep=", ")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif command == "cd":
            if argument == "":
                try:
                    os.chdir(os.path.expanduser("~"))
                    print(f"Current path: {os.getcwd()}")
                except Exception as e:
                    print(f"An error occurred: {e}")
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
                    if argument_2 == "":
                        os.rmdir(argument)
                        print(f"Directory '{argument}' removed")
                    elif argument_2 == "-r":
                        shutil.rmtree(argument)
                        print(f"Directory '{argument}' removed")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif command == "exit":
            print("Bye!")
            break

        else:
            print("Unknown command")

main()
