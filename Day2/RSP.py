# import rich console
from rich.console import Console

def main():
    f = open("input.txt", "r")

    console = Console()

    total_score = 0

    rock_paper_scissors = {"A": {"X": 4, "Y": 8, "Z": 3}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 7, "Y": 2, "Z": 6}}

    # PART 1
    for line in f:
        line = line.strip().split(" ")
        total_score += rock_paper_scissors[line[0]][line[1]]


    console.print(f"Total Score: {total_score}")

    # PART 2
    total_score = 0
    rock_paper_scissors = {"A": {"X": 3, "Y": 4, "Z": 8}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 2, "Y": 6, "Z": 7}}

    f1 = open("input.txt", "r")

    for line in f1:
        line = line.strip().split(" ")
        total_score += rock_paper_scissors[line[0]][line[1]]

    console.print(total_score)
    


if __name__ == "__main__":
    main()