import os
def main():
    lines = []
    sum = 0
    f = open("input.txt", "r")
    for line in f:
        if line == '\n':
            lines.append(sum)
            sum = 0
        else:
            line_copy = line.rstrip('\n')
            sum += int(line_copy)
    lines.sort(reverse=True)
    best_3 = lines[0] + lines[1] + lines[2]
    f.close()
    print(best_3)
main()