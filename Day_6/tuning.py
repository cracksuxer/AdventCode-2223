from rich.console import Console
from rich.traceback import install

install()

def main():
    console = Console()
    
    file = open("input.txt", "r")

    packets = list(map(str, file.read().split("\n")))
    file.close()

    for packet in packets:
        start, packet_len = 0, 0
        packet_len = 0
        while packet_len != 14:
            # ------ PART 1 ------ #
            # first_four = packet[start:start+4]
            # ------ PART 2 ------ #
            packet_len = len(dict.fromkeys(packet[start:start+14]))
            start += 1
        console.print("First 14 unique characters starts at {} letter[/]".format(start+13))

if __name__ == "__main__":
    main()