from collections import deque
from copy import copy


INPUT = "input.txt"

CYCLE_COST = {
    "noop": 1,
    "addx": 2
}


### Input Processing ###

def build_commands(path_in):
    commands = deque()
    with open(path_in, "r") as file:
        for line in file.readlines():
            unzipped = line.strip().split()
            cost = CYCLE_COST[unzipped[0]]
            value = 0 if len(unzipped) == 1 else int(unzipped[1])
            commands.append((cost, value))
    return commands


### Part One ###

def sum_signal_values(commands, start, stop, difference):
    output = 0
    register, cycle = 1, 1
    remaining, value = 0, 0
    signal = start

    while commands and signal <= stop:
        if remaining == 0:
            register += value
            remaining, value = commands.popleft()
        if cycle == signal:
            output += signal * register
            signal += difference
        remaining -= 1
        cycle += 1

    return output


### Part Two ###

def draw_crt(commands):
    output = ""
    register, cycle = 1, 1
    remaining, value = 0, 0

    while commands:
        if remaining == 0:
            register += value
            remaining, value = commands.popleft()
        output += "#" if is_sprite_on_pixel((cycle - 1) % 40, register) else " "
        remaining -= 1
        cycle += 1

    return output


def format_crt(crt, width=40):
    rows = []
    start = 0
    stop = width
    while stop <= len(crt):
        rows.append(crt[start:stop])
        start += width
        stop += width
    return "\n".join(rows)


def is_sprite_on_pixel(pixel, register):
    return register - 1 <= pixel <= register + 1


def get_sprite_range(center):
    return center - 1, center, center + 1


### Execution ###

if __name__ == "__main__":
    instructions = build_commands(INPUT)

    # Part One
    print(sum_signal_values(copy(instructions), 20, 220, 40))

    # Part Two
    drawn = draw_crt(copy(instructions))
    formatted = format_crt(drawn)
    print(formatted, "")
