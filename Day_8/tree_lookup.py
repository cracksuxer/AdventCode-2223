from rich.console import Console
from rich import print
from rich.traceback import install
import numpy as np

install()
console = Console()


# ----- PART 1 ----- #
def look_up_tree(matrix: np.ndarray, x: int, y: int) -> bool:
    right = matrix[x, y + 1:]
    left = matrix[x, :y]
    up = matrix[:x, y]
    down = matrix[x + 1:, y]

    left = np.flip(left)
    up = np.flip(up)

    return np.any(right >= matrix[x, y]) and np.any(left >= matrix[x, y]) and np.any(up >= matrix[x, y]) and np.any(down >= matrix[x, y])

# ----- PART 2 ----- #
def viewing_distance(matrix: np.ndarray, x: int, y: int) -> int:
    right = matrix[x, y + 1:]
    left = matrix[x, :y]
    up = matrix[:x, y]
    down = matrix[x + 1:, y]

    left = np.flip(left)
    up = np.flip(up)

    # right
    for i in range(len(right)):
        if right[i] >= matrix[x, y]:
            right = right[:i + 1]
            break
    # left
    for i in range(len(left)):
        if left[i] >= matrix[x, y]:
            left = left[:i + 1]
            break
    # up
    for i in range(len(up)):
        if up[i] >= matrix[x, y]:
            up = up[:i+1]
            break
    # down
    for i in range(len(down)):
        if down[i] >= matrix[x, y]:
            down = down[:i + 1]
            break

    return len(right) * len(left) * len(up) * len(down) 

def main():

    file = open("input.txt", "r")
    output = open("output.txt", "w")

    for line in file:
        split_digits = ""
        for digit in line.strip():
            if digit != " ":
                split_digits += digit + ","
        split_digits = split_digits[:-1]
        output.write("".join(split_digits) + "\n")

    output.close()
    file.close()

    input = np.loadtxt("output.txt", delimiter=",", dtype=int)

    # visible_trees = 2 * (input.shape[0] + input.shape[1]) - 4
    best_tree = {"pos": [0, 0], "value": 0}

    for i in range(input.shape[0]):
        if i == 0 or i == input.shape[0] - 1:
            continue
        for j in range(input.shape[1]):
            if j == 0 or j == input.shape[1] - 1:
                continue
            # if look_up_tree(input, [i, j]):
                # print(f"Found a tree: {input[i, j]}")
                # visible_trees += 1
            
            current = viewing_distance(input, i, j)
            if current > best_tree["value"]:
                best_tree["value"] = current
                best_tree["pos"] = [i, j]

    #  print(f"Found {visible_trees} trees in the matrix")
    print(f"Best tree: {best_tree['value']} at position {best_tree['pos']}")

    
if __name__ == "__main__":
    main()