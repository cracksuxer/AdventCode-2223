from rich.console import Console
import re

# print ranges in this form lengh 9:
# 
# ...456789
# 123......
# ....5....
# 1........
# returns string
def range_print(range_list):
    start = range_list[0]
    end = range_list[1]
    console = Console()
    console.print(" " * start + "." * (end - start + 1), style="bold green")
    

def main():
    console = Console()
    file = open("input.txt", "r")

    sets = []

    for line in file:
        line_s = line.strip().split(",")
        set = []
        for i in line_s:
            res = re.findall('[0-9]+', i)
            if res:
                set.append(res)
        sets.append(set)

    for i in range(len(sets)):
        for j in range(len(sets[i])):
            sets[i][j] = [int(x) for x in sets[i][j]]

    # inside_sets = 0

    # for i in range(len(sets)):
    #     console.print("{} >= {} and {} <= {} or {} >= {} and {} <= {}".format(sets[i][0][0], sets[i][1][0], sets[i][0][1], sets[i][1][1], sets[i][1][0], sets[i][0][0], sets[i][1][1], sets[i][0][1]))
    #     if sets[i][0][0] >= sets[i][1][0] and sets[i][0][1] <= sets[i][1][1] or sets[i][1][0] >= sets[i][0][0] and sets[i][1][1] <= sets[i][0][1]:
    #         inside_sets += 1
        
    # console.print(inside_sets)

    overlap_sets = 0

    for i in range(len(sets)):
        # range_print(sets[i][0])
        # range_print(sets[i][1])
        if not(sets[i][0][0] < sets[i][1][0] and sets[i][0][1] < sets[i][1][0] or sets[i][0][0] > sets[i][1][1] and sets[i][0][1] > sets[i][1][1]):
            overlap_sets += 1
            console.print("overlap", style="bold red")

    console.print(overlap_sets)

if __name__ == "__main__":
    main()