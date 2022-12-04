from rich.console import Console


def get_value(char):
    if char.isalpha():
        if char.islower():
            return ord(char) - 96
        else:
            return ord(char) - 38
    else:
        return 0

def main():

    # console = Console()
    # file = open("test.txt", "r")
 
    # total_sum = 0

    # for line in file:
    #     line_s = line.replace("\n", "")
    #     half_lenght = len(line_s) // 2
    #     half_1 = line_s[:half_lenght]
    #     half_2 = line_s[half_lenght:]
            
    #     symbols = {}

    #     for char in half_1:
    #         if half_2.find(char) != -1:
    #             symbols[char] =  get_value(char)

    #     if len(symbols) > 0:
    #         console.print(symbols)
    #         total_sum += sum(symbols.values())

    #     console.print("\n")

    # console.print(total_sum)

    console = Console()
    
    file = open("input.txt", "r")

    lines = len(file.readlines()) // 3

    file.seek(0)


    total_sum = 0

    console.log(log_locals=True)

    for i in range(lines):
        line_1 = file.readline().replace("\n", "")
        line_2 = file.readline().replace("\n", "")
        line_3 = file.readline().replace("\n", "")

        symbols = {}
        
        for char in line_1:
            if line_2.find(char) != -1 and line_3.find(char) != -1:
                console.print(char, end=" ")
                symbols[char] = get_value(char)

        if len(symbols) > 0:
            console.print(symbols)
            total_sum += sum(symbols.values())

        console.print("\n")

    console.print(total_sum)


if __name__ == '__main__':
    main()