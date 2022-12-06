from bisect import insort


INPUT_PATH = "input.txt"


def take_inventory(path_in):
    elves = []
    with open(path_in, "r") as inp:
        elf = 0
        for line in inp.readlines():
            if line == "\n":
                insort(elves, elf)  # Inserts 'elf' at such a position that the sequence remains sorted.
                elf = 0
            else:
                elf += int(line.strip())

    return elves


def get_top_elves(elves, number_of_elves):
    total = 0
    for i in range(-number_of_elves, 0):
        total += elves[i]
    return total


if __name__ == "__main__":
    inventory = take_inventory(INPUT_PATH)

    # Part One
    print(f"Top Elf: {get_top_elves(inventory, 1)}")

    # Part Two
    print(f"Top 3: {get_top_elves(inventory, 3)}")
