from itertools import product


INPUT = "input.txt"


def build_table(path_in):
    with open(path_in, "r") as file:
        table = tuple(
            tuple(
                int(c) for c in line.strip()
            ) for line in file.readlines()
        )
        return table


def get_row_section(table, row, start, stop):
    return table[row][start:stop]


def get_column_section(table, column, start, stop):
    length = len(table)
    return tuple(
        table[row][column] for row in range(length) if start <= row < stop
    )


def get_visible_cells(table):
    max_x = len(table[0]) - 1
    max_y = len(table) - 1
    visible = get_edge_cells(max_x, max_y)

    coordinates = product(
        range(1, max_x),
        range(1, max_y)
    )
    for x, y in coordinates:
        if is_cell_visible(table, x, y, max_x, max_y):
            visible.add((x, y))

    return visible


def get_scenic_scores(table):
    max_x = len(table[0]) - 1
    max_y = len(table) - 1
    scores = []

    coordinates = product(
        range(1, max_x),
        range(1, max_y)
    )
    for x, y in coordinates:
        score = get_scenic_score(table, x, y, max_x, max_y)
        scores.append(score)

    return scores


def get_edge_cells(max_x, max_y):
    edges = set()
    edges |= set(product(range(max_x + 1), (0, max_y)))
    edges |= set(product((0, max_x), range(max_y + 1)))
    return edges


def get_scenic_score(table, x, y, max_x, max_y):
    cell = table[y][x]

    left = get_viewable_distance(cell, get_row_section(table, y, 0, x)[::-1])
    right = get_viewable_distance(cell, get_row_section(table, y, x + 1, max_x + 1))
    above = get_viewable_distance(cell, get_column_section(table, x, 0, y)[::-1])
    below = get_viewable_distance(cell, get_column_section(table, x, y + 1, max_y + 1))

    return left * right * above * below


def is_cell_visible(table, x, y, max_x, max_y):
    cell = table[y][x]

    left = get_row_section(table, y, 0, x)
    right = get_row_section(table, y, x + 1, max_x + 1)
    above = get_column_section(table, x, 0, y)
    below = get_column_section(table, x, y + 1, max_y + 1)

    return cell > true_max(left) or cell > true_max(right) or cell > true_max(above) or cell > true_max(below)


def true_max(iterable):
    if iterable:
        return max(iterable)
    return 0


def get_viewable_distance(height, direction):
    distance = 0
    for tree in direction:
        distance += 1
        if tree >= height:
            break
    return distance


if __name__ == "__main__":
    forest = build_table(INPUT)
    print(len(get_visible_cells(forest)))  # Part 1
    print(max(get_scenic_scores(forest)))  # Part 2