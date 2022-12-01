import os
def main():
    f = open("input.txt", "r")

    # elves_calories = []
    # calories_sum = 0

    # for line in f:
    #     if line == '\n':
    #         elves_calories.append(calories_sum)
    #         calories_sum = 0
    #     else:
    #         line_copy = line.rstrip('\n')
    #         calories_sum += int(line_copy)


    # Pure functional

    elves_calories = sum(sorted(list(map(lambda x: sum(map(int, x.splitlines())), f.read().split('\n\n'))), reverse=True)[:3])
    f.close()
    print(elves_calories)


main()