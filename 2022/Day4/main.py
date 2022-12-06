from itertools import chain


INPUT = "input.txt"


### Input Processing ###

def unzip_line(line):
    # We do not speak of this unholy one-liner. It is nasty, but it does the heavy lifting.
    return tuple(map(int, chain(*(x.split("-") for x in line.split(",")))))


def build_pairs(path_in):
    pairs = []

    with open(path_in, "r") as input_file:

        for line in input_file.readlines():
            stripped = line.strip()
            if stripped:
                unzipped = unzip_line(stripped)
                pair = unzipped[:2], unzipped[2:]
                pairs.append(pair)

    return pairs


### Part One ###

def is_subrange(sub_start, sub_stop, super_start, super_stop):
    return sub_start >= super_start and sub_stop <= super_stop


def is_subrange_in_pair(pair):
    (w, x), (y, z) = pair
    return is_subrange(w, x, y, z) or is_subrange(y, z, w, x)


### Part Two ###

def is_overlap(first_start, first_stop, second_start, second_stop):
    return first_start <= second_stop and first_stop >= second_start


def is_overlap_in_pair(pair):
    (w, x), (y, z) = pair
    return is_overlap(w, x, y, z) and is_overlap(y, z, w, x)


### Execution ###

def sum_confirmations(pairs, predicate):
    return sum(
        int(predicate(pair)) for pair in pairs
    )


if __name__ == "__main__":
    elf_pairs = build_pairs(INPUT)
    print(sum_confirmations(elf_pairs, is_overlap_in_pair))
