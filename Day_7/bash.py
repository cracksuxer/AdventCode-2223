from rich.console import Console
from rich.traceback import install
from rich.tree import Tree

install()
console = Console()

def find_key(d, key):
    for k, v in d.items():
        if k == key:
            return v
        if isinstance(v, dict):
            item = find_key(v, key)
            if item is not None:
                return item
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    item = find_key(i, key)
                    if item is not None:
                        return item


# Print name and size of diretories if the total size is less than 100000
# If a directory is empty, total size is 0
def find_dirs(d):
    for k, v in d.items():
        if isinstance(v, list):
            total_size = 0
            for i in v:
                if isinstance(i, dict):
                    for k1, v1 in i.items():
                        if isinstance(v1, int):
                            total_size += v1
            if total_size < 100000:
                console.log(k, total_size)
        if isinstance(v, dict):
            find_dirs(v)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    find_dirs(i)


def main():


    file = open("input.txt", "r")
    directory = {"/": []}
    current_dir = ""
    flag_ls = False

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
            current_folder = current_dir.split('/')[-1]
            if current_folder == "":
                current_folder = '/'
            if line_s[0] == "dir":
                find_key(directory, current_folder).append({line_s[1]: []})
            else :
                find_key(directory, current_folder).append({line_s[1]: int(line_s[0])})

    console.log("Directory: ", directory)

    find_dirs(directory)


if __name__ == "__main__":
    main()