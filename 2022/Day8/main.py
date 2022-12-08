from functools import reduce


INPUT = "input.txt"


def build_table(path_in):
    table = []
    with open(path_in, "r") as file:
        for line in file.readlines():
            stripped = line.strip()
            table.append(
                tuple(int(c) for c in stripped)
            )

    return table


def view_table(table):
    for row in table:
        print(row)
    print("\n")


def get_all_visible(table):
    sets = (
        get_visible(table),
        get_visible(table, rotated=True),
        get_visible(table, inverted=True),
        get_visible(table, inverted=True, rotated=True),
    )
    return set(reduce(set.union, sets))


def get_visible(table, rotated=False, inverted=False):
    output = set()
    table = format_table(table, rotated, inverted)

    max_x = len(table[0])
    max_y = len(table)

    for y in range(max_y):
        max_height = -1
        for x in range(max_x):

            cell = table[y][x]
            if cell > max_height:
                formatted = format_coordinates(x, y, max_x, max_y, rotated, inverted)
                output.add(formatted)
            max_height = max(max_height, cell)

    return output


def format_table(table, rotated, inverted):
    formatted = table
    if rotated:
        formatted = rotate_table(formatted)
    if inverted:
        formatted = [row[::-1] for row in formatted]
    return formatted


def format_coordinates(x, y, max_x, max_y, rotated=False, inverted=False):
    if inverted:
        x = max_x - (x + 1)
    if rotated:
        x, y = max_y - (y + 1), x
    return x, y


def rotate_table(table):
    return list(zip(*table[::-1]))


if __name__ == "__main__":
    forest = build_table(INPUT)
    trees = get_all_visible(forest)
    print(len(trees))
