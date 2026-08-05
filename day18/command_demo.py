class Folder:
    def __init__(self, name):
        self.name = name
        self.parent # None 代表他是根節點 root
        self.children = []

class File:
    def __init__(self, name):
        self.name = name

def all_descendant(folder, depth = 0):
    print("    " * depth + folder.name)

    child = folder.children[0]
    
    all_descendant(child, depth + 1)



# 手動建立一些預設的節點
root = Folder('root')
folder1 = Folder('day1')
folder2 = Folder('day2')
folder3 = Folder('day3')
folder4 = Folder('day4')
folder5 = Folder('day5')

folders = [Folder(f'day{i+1}') for i in range(5)]

root.children.append(folder1)
root.children.append(folders[0])

file1 = File('test.txt')

root.children.append(file1)


# 
while True:

    command = input("> ").strip()

    if command == "":
        continue

    parts = command.split()     # cd ..
    action = parts[0].lower()

    if action == "hi":
        print('hi')
    if action == "cd":
        print()
    if action == "tree":        # descendant
        all_descendant(folder)
        pass
    else:
        print("\033[31m無法辨識\033[0m")