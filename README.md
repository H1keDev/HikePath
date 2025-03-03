# HikePath
A simple command-line file manager built in Python
## Requirements:
- Python 3
## Installing (for linux):
Use git clone:
```
git clone https://github.com/H1keDev/HikePath.git
```
Go to the cloned directory:
```
cd HikePath
```
And start the main file:
```
python3 hikepath.py
```
## Using:
Commands list:

| Command                   | Description                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| `ls` (or `dir`)            | List files and folders in the current directory or at `<path>`                                |
| `cd <path>`                | Change to directory `<path>`                                                                  |
| `mkdir <name>`             | Create a new directory `<name>`                                                                |
| `rmdir <name> <argument>`  | Remove directory `<name>`. Use `-r` for recursive removal.                                     |
| `exit`                     | Exit the program                                                                               |
| `help`                     | Show this help message                                                                          |
| `history`                  | Show the last 5 commands                                                                       |

### Note:
- When using `cd`, if no path is specified, it defaults to the home directory.
- Use `rmdir` without `-r` for non-recursive deletion (only empty directories).
- Errors may occur if a directory or file does not exist or if there are permission issues.

