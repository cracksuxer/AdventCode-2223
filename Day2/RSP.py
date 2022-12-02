# import rich console
from rich.console import Console

def main():
    f = open("input.txt", "r")

    console = Console()

    total_score = 0

    # for line in f:
    #     line = line.strip().split(" ")
    #     if line[0] == 'A':
    #         if line[1] == 'X':
    #             total_score += 1 + 3
    #         if line[1] == 'Y':
    #             total_score += 2 + 6
    #         if line[1] == 'Z':
    #             total_score += 3 + 0
    #     elif line[0] == 'B':
    #         if line[1] == 'X':
    #             total_score += 1 + 0
    #         if line[1] == 'Y':
    #             total_score += 2 + 3
    #         if line[1] == 'Z':
    #             total_score += 3 + 6
    #     elif line[0] == 'C':
    #         if line[1] == 'X':
    #             total_score += 1 + 6
    #         if line[1] == 'Y':
    #             total_score += 2 + 0
    #         if line[1] == 'Z':
    #             total_score += 3 + 3


    for line in f:
        line = line.strip().split(" ")
        if line[0] == 'A':
            if line[1] == 'X':
                total_score += 3 + 0
            if line[1] == 'Y':
                total_score += 1 + 3
            if line[1] == 'Z':
                total_score += 2 + 6
        elif line[0] == 'B':
            if line[1] == 'X':
                total_score += 1 + 0
            if line[1] == 'Y':
                total_score += 2 + 3
            if line[1] == 'Z':
                total_score += 3 + 6
        elif line[0] == 'C':
            if line[1] == 'X':
                total_score += 2 + 0
            if line[1] == 'Y':
                total_score += 3 + 3
            if line[1] == 'Z':
                total_score += 1 + 6

    console.print(total_score)
    


if __name__ == "__main__":
    main()