# modulize code into different files


class FileSystemItem:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def get_path(self):
        if self.parent is None:
            return "/"

        parts = []
        current = self

        while current.parent is not None:
            parts.append(current.name)
            current = current.parent

        return "/" + "/".join(reversed(parts))


class File(FileSystemItem):
    def __init__(self, name, parent=None, content=""):
        super().__init__(name, parent)
        self.content = content


class Folder(FileSystemItem):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        item.parent = self

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_item(self, name):
        return self.items.get(name)


class VirtualTerminal:
    def __init__(self):
        self.root = Folder("/")
        self.current = self.root

    def resolve_path(self, path):
        if path == "/":
            return self.root

        if path.startswith("/"):
            current = self.root
            parts = path.split("/")
        else:
            current = self.current
            parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue

            if part == "..":
                if current.parent is not None:
                    current = current.parent
                continue

            if not isinstance(current, Folder):
                return None

            if part not in current.items:
                return None

            current = current.items[part]

        return current

    def pwd(self):
        print(self.current.get_path())

    def ls(self):
        if not self.current.items:
            print("(empty)")
            return

        for item in self.current.items.values():
            if isinstance(item, Folder):
                print(item.name + "/")
            else:
                print(item.name)

    def cd(self, path):
        target = self.resolve_path(path)

        if target is None:
            print("Error: path not found")
            return

        if not isinstance(target, Folder):
            print("Error: not a directory")
            return

        self.current = target

    def mkdir(self, name):
        if "/" in name:
            print("Error: invalid folder name")
            return

        if name in self.current.items:
            print("Error: item already exists")
            return

        folder = Folder(name)
        self.current.add_item(folder)

    def touch(self, name):
        if "/" in name:
            print("Error: invalid file name")
            return

        if name in self.current.items:
            print("Error: item already exists")
            return

        file = File(name)
        self.current.add_item(file)

    def cat(self, name):
        item = self.resolve_path(name)

        if item is None:
            print("Error: file not found")
            return

        if not isinstance(item, File):
            print("Error: not a file")
            return

        print(item.content)

    def write(self, name, text):
        item = self.resolve_path(name)

        if item is None:
            print("Error: file not found")
            return

        if not isinstance(item, File):
            print("Error: not a file")
            return

        item.content = text

    def rm(self, name):
        item = self.current.get_item(name)

        if item is None:
            print("Error: file not found")
            return

        if not isinstance(item, File):
            print("Error: use rmdir for folders")
            return

        self.current.remove_item(name)

    def rmdir(self, name):
        item = self.current.get_item(name)

        if item is None:
            print("Error: folder not found")
            return

        if not isinstance(item, Folder):
            print("Error: not a folder")
            return

        if item.items:
            print("Error: folder is not empty")
            return

        self.current.remove_item(name)

    def tree(self, folder=None, prefix=""):
        if folder is None:
            folder = self.current
            print(folder.name)

        items = list(folder.items.values())

        for i, item in enumerate(items):
            last = i == len(items) - 1

            if last:
                connector = "└── "
            else:
                connector = "├── "

            print(prefix + connector + item.name)

            if isinstance(item, Folder):
                if last:
                    new_prefix = prefix + "    "
                else:
                    new_prefix = prefix + "│   "

                self.tree(item, new_prefix)

    def help(self):
        print("""
Available commands:

ls
    Show files and folders

pwd
    Show current path

cd <folder>
    Enter a folder

cd ..
    Go back one folder

cd /
    Go to root

mkdir <name>
    Create a folder

touch <name>
    Create a file

cat <file>
    Read a file

write <file> <text>
    Write text into a file

rm <file>
    Delete a file

rmdir <folder>
    Delete an empty folder

tree
    Display folder structure

clear
    Clear the screen

help
    Show this menu

exit
    Close the terminal
""")

    def run(self):
        print("Virtual Python Terminal")
        print("Type 'help' for commands.")
        print()

        while True:
            command = input(self.current.get_path() + " $ ").strip()

            if command == "":
                continue

            parts = command.split()

            main_command = parts[0]

            if main_command == "exit":
                print("Terminal closed.")
                break

            elif main_command == "help":
                self.help()

            elif main_command == "pwd":
                self.pwd()

            elif main_command == "ls":
                self.ls()

            elif main_command == "tree":
                self.tree()

            elif main_command == "clear":
                print("\n" * 50)

            elif main_command == "cd":
                if len(parts) < 2:
                    print("Usage: cd <folder>")
                else:
                    self.cd(parts[1])

            elif main_command == "mkdir":
                if len(parts) < 2:
                    print("Usage: mkdir <folder>")
                else:
                    self.mkdir(parts[1])

            elif main_command == "touch":
                if len(parts) < 2:
                    print("Usage: touch <file>")
                else:
                    self.touch(parts[1])

            elif main_command == "cat":
                if len(parts) < 2:
                    print("Usage: cat <file>")
                else:
                    self.cat(parts[1])

            elif main_command == "write":
                if len(parts) < 3:
                    print("Usage: write <file> <text>")
                else:
                    filename = parts[1]
                    text = " ".join(parts[2:])
                    self.write(filename, text)

            elif main_command == "rm":
                if len(parts) < 2:
                    print("Usage: rm <file>")
                else:
                    self.rm(parts[1])

            elif main_command == "rmdir":
                if len(parts) < 2:
                    print("Usage: rmdir <folder>")
                else:
                    self.rmdir(parts[1])

            else:
                print(f"Command not found: {main_command}")


terminal = VirtualTerminal()
terminal.run()