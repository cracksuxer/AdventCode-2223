from rich.console import Console

def main():
    console = Console()
    
    file = open("input.txt", "r")

    packets = list(map(str, file.read().split("\n")))
    file.close()

    for packet in packets:
        start = 0
        first_four = ""
        packet_len = 0
        while packet_len != 14:
            # ------ PART 1 ------ #
            # first_four = packet[start:start+4]
            # ------ PART 2 ------ #
            first_14 = packet[start:start+14]
            packet_len = len(dict.fromkeys(first_14))
            start += 1
        console.print("First 14 unique characters starts at {} letter: [green]{}[/]".format(start+13, first_four))

if __name__ == "__main__":
    main()