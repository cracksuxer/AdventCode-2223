from rich.console import Console
from rich.traceback import install
from rich import print

install()
console = Console()

class File:
    def __init__(self, name, parent: 'Folder', size : int = 0):
        self._name = name
        self._size = size
        self._parent = parent

    def __str__(self):
        return f"File: {self.name}, Size: {self.size}"

    def __repr__(self):
        return f"File: {self.name}, Size: {self.size}"

    @property
    def name(self):
        return self._name
    @property
    def size(self):
        return self._size
    @property
    def parent(self):
        return self._parent
    @name.setter
    def name(self, name):
        self._name = name
    @size.setter
    def size(self, size):
        self._size = size
    @parent.setter
    def parent(self, parent):
        self._parent = parent

class Folder:
    def __init__(self, name: str, subfolders: list, path: str, parent: 'Folder', size : int = 0) -> None:
        self._name = name
        self._subfolders = subfolders
        self._path = path
        self._size = size
        self._parent = parent

    def __str__(self) -> str:
        return f"Folder: {self.name}, Size: {self.size}, Subfolders: {self.subfolders}"

    def __repr__(self) -> str:
        return f"Folder: {self.name}, Size: {self.size}, Subfolders: {self.subfolders}"

    def tree_print(self, level: int = 0) -> None:
        parent_name = self.parent.name if self.parent else "None"
        print(f"{'    ' * level}[bold yellow]{self.name}[/] ({self.size}) <- [yellow]{parent_name}[/]") if self.name != '/' else print(f"[bold purple]{self.name}[/] ({self.size})")
        for i in self.subfolders:
            if isinstance(i, Folder):
                i.tree_print(level + 1)
            else:
                parent_name = i.parent.name if i.parent else "None"
                print(f"{'    ' * (level + 1)}[bold green]{i.name}[/] ({i.size}) <- [yellow]{parent_name}[/]")
        
    def search_folder(self, name: str) -> 'Folder':
        if self.name == name:
            return self
        for i in self.subfolders:
            if isinstance(i, Folder):
                if i.name == name:
                    return i
                else:
                    return i.search_folder(name)
            else:
                return None

    def search_by_path(self, path: str) -> 'Folder':
        if path == '/':
            return self
        if path == None:
            return None
        key_to_find = path.split('/')[1]
        for i in self.subfolders:
            if isinstance(i, Folder):
                if i.name == key_to_find:
                    if len(path.split('/')) == 2:
                        return i
                    else:
                        return i.search_by_path("/" + ''.join(path.split('/', 2)[2:]))
        
        raise Exception(f"Folder {key_to_find} not found")
            
    def add_folder(self, folder: 'Folder') -> None:
        self.subfolders.append(folder)
        self.size = self.calc_size()

        parent = self.parent
        while parent:
            parent.size += folder.size
            parent = parent.parent

    def add_file(self, file) -> None:
        self.subfolders.append(file)
        self.size = self.calc_size()

        parent = self.parent
        while parent:
            parent.size += file.size
            parent = parent.parent

    def calc_size(self) -> int:
        total_size = 0
        for i in self.subfolders:
            if isinstance(i, Folder):
                total_size += i.calc_size()
            else:
                total_size += i.size
        return total_size
        
    @property
    def size(self) -> int:
        return self._size
    @property
    def path(self) -> str:
        return self._path
    @property
    def name(self) -> str:
        return self._name
    @property
    def subfolders(self) -> list:
        return self._subfolders
    @property
    def parent(self) -> 'Folder':
        return self._parent
    @size.setter
    def size(self, size: int) -> None:
        self._size = size
    @path.setter
    def path(self, path: str) -> None:
        self._path = path
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    @subfolders.setter
    def subfolders(self, subfolders: list) -> None:
        self._subfolders = subfolders
    @parent.setter
    def parent(self, parent: 'Folder') -> None:
        self._parent = parent


def main():
    directory = Folder("/", [], "/", None)
    current_dir = ""
    flag_ls = False

    file = open("input.txt", "r")

    for line in file:
        line_s = line.strip().split()
        if line.startswith("$"):
            if line_s[1] == 'cd':
                flag_ls = False
                if line_s[2] == '..':
                    current_dir = current_dir.rsplit('/', 1)[0]
                    if current_dir == '':
                        current_dir = '/'
                else:
                    if line_s[2] == '/':
                        current_dir = "/"
                    elif current_dir == '/':
                        current_dir += line_s[2]  
                    else: 
                        current_dir += "/" + line_s[2]
            elif line_s[1] == 'ls':
                flag_ls = True
        elif flag_ls == True:
            if line_s[0] == "dir":
                directory.search_by_path(current_dir).add_folder(Folder(line_s[1], [], current_dir, directory.search_by_path(current_dir)))
            else :
                directory.search_by_path(current_dir).add_file(File(line_s[1], directory.search_by_path(current_dir), int(line_s[0])))

    file.close()
    directory.tree_print()

    total_space = directory.size
    max_space = 70000000
    space_needed = 30000000
    unused_space = max_space - total_space
    need_to_delete = space_needed - unused_space

    def list_folders(d, update) -> int:
        folders = []
        for i in d.subfolders:
            if isinstance(i, Folder):
                if i.size >= update:
                    folders.append(i.size)
                folders += list_folders(i, update)
        return folders

    console.log(min(list_folders(directory, need_to_delete), key=lambda x:abs(x-6876531)))
    
if __name__ == "__main__":
    main()