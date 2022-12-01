import os
def main():
    elves_calories = []
    calories_sum = 0

    f = open("input.txt", "r")

    for line in f:
        if line == '\n':
            elves_calories.append(calories_sum)
            calories_sum = 0
        else:
            line_copy = line.rstrip('\n')
            calories_sum += int(line_copy)
            
    f.close()
    three_best_sum = sum(sorted(elves_calories, reverse=True)[:3])
    print(three_best_sum)


main()