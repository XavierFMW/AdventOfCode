from collections import deque


INPUT = "input.txt"


### Input Processing ###

def build_contents_from_diagram(diagram):
    length = len(diagram[0])
    contents = []
    index = 1

    while index <= length:
        stacked = ""
        for layer in diagram[::-1]:
            c = layer[index]
            if c.isalpha():
                stacked += c
        contents.append(stacked)
        index += 4

    return contents


def build_steps(lines):
    steps = []
    for line in lines:
        quantity, source, destination = [int(i) for i in line.split() if i.isnumeric()]
        steps.append((quantity, source - 1, destination - 1))
    return steps


def build_stacks(diagram):
    stacks = [deque(c) for c in build_contents_from_diagram(diagram)]
    return stacks


def process_input(text):
    header, body = [section.split("\n") for section in text.split("\n\n")]
    formatted_header = header[:-1]
    return formatted_header, body


def get_stacks_and_steps(path_in):
    with open(path_in, "r") as file:
        diagram, instructions = process_input(file.read())
        stacks = build_stacks(diagram)
        steps = build_steps(instructions)
        return stacks, steps


### Part One ###

def move_unordered(source, destination, quantity):
    for _ in range(quantity):
        item = source.pop()
        destination.append(item)


### Part Two ###

def move_ordered(source, destination, quantity):
    order = []
    for _ in range(quantity):
        order += source.pop()

    for item in order[::-1]:
        destination.append(item)


### Shared Functions ###

def get_top_of_stacks(stacks):
    output = ""
    for stack in stacks:

        try:
            char = stack.pop()
            output += char
        except IndexError:
            continue

    return output


def shift_items(steps, stacks, ordered=False):
    move = move_ordered if ordered else move_unordered
    for step in steps:
        quantity, source, destination = step
        move(stacks[source], stacks[destination], quantity)


### Execution ###

if __name__ == "__main__":
    crates, procedure = get_stacks_and_steps(INPUT)
    shift_items(procedure, crates, ordered=True)  # Change "ordered" argument for each part.
    print(get_top_of_stacks(crates))
