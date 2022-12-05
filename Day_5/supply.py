from rich.console import Console
from re import findall

console = Console()

def print_stacks(stacks):
    for i in range(len(stacks)):
        print("Stack", i, stacks[i])

def move(stacks, move):
    console = Console()
    move = move.split("->")
    move = list(map(int, move[0].split(" ") + move[1].split(" ")))

    n_cages = move[0]
    from_stack = move[1] - 1
    to_stack = move[2] - 1

    # ------- Part 1 ------- #

    # for _ in range(n_cages):
    #     console.print("[green]Moving [red][{}][/]: [cyan]{}[/] -> [cyan]{}[/][/]".format(stacks[from_stack][-1], from_stack+1, to_stack+1))
    #     stacks[to_stack].append(stacks[from_stack].pop())

    # ------- Part 2 ------- #
    if n_cages == 1:
        console.print("[green]Moving [red][{}][/]: [cyan]{}[/] -> [cyan]{}[/][/]".format(stacks[from_stack][-1], from_stack+1, to_stack+1))
        stacks[to_stack].append(stacks[from_stack].pop())
    else:
        console.print("Moving {} cages from stack {} to stack {}".format(n_cages, from_stack, to_stack), style="green")
        stacks[to_stack].extend(stacks[from_stack][-n_cages:])
        stacks[from_stack] = stacks[from_stack][:-n_cages]

    print_stacks(stacks)

def main():
    file = open("input.txt", "r")

    line, drawing = "", ""
    moves, stacks = [], []

    while line != '\n':
        line = file.readline()
        drawing += line.replace("    \n", " [#]\n").replace("    ", "[#] ")

    moves = list(map(lambda x: x.strip().replace("move ", "").replace("from ", "").replace(" to ", "->"), file.readlines()))
    drawing = list(filter(None, drawing.replace(" ", "").split()))
    stacks = [[] for _ in range(int(drawing[-1][-1].strip()))]

    for i in range(len(drawing)-1, -1, -1):
        letter = findall(r'\[(.*?|)\]', drawing[i])
        for j in range(len(letter)):
            if letter[j] != "#":
                stacks[j].append(letter[j])

    list(map(lambda u_mov: move(stacks, u_mov), moves))
    top_letters = map(lambda x: x[-1], stacks)
    console.print("\n\n[green]The top letters are: [red]{}[/]".format("".join(top_letters)))


if __name__ == "__main__":
    main()