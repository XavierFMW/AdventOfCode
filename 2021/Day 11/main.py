
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    matrix = []
    for line in input:
        matrix.append([int(x) for x in line.strip()])


# Define key functions

def print_matrix(matrix):

    for row in matrix:
        print(row)
    print("\n")


def increment_matrix(matrix):

    for index, row in enumerate(matrix):
        matrix[index] = [x + 1 for x in row]


def flash(starting_point, matrix):

    x, y = starting_point
    matrix[y][x] += 1

    if x > 9 or x < 0 or y > 9 or y < 0:
        return

    secondary_flashes = []
    points = [
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    for point in points:

        x, y = point
        if x >= 0 and y >= 0:

            try:
                matrix[y][x] += 1

                if matrix[y][x] == 10:
                    secondary_flashes.append(point)

            except IndexError:
                pass

    for point in secondary_flashes:
        flash(point, matrix)


def check_initial_flashes(matrix):

    initial_flashes = []

    for y, row in enumerate(matrix):
        for x, value in enumerate(row):

            if value == 10:
                initial_flashes.append((x, y))

    for point in initial_flashes:
        flash(point, matrix)


# Run simulation

flashes = 0
steps = 0

while sum([num for row in matrix for num in row]) > 0:

    increment_matrix(matrix)
    check_initial_flashes(matrix)
    
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):

            if value >= 10:
                matrix[y][x] = 0
                flashes += 1

    steps += 1
