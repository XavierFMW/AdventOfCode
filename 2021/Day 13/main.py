
# Recieve Input from File

with open("input.txt", "r") as file:
    points, instrcutions = [], []
    max_x, max_y = 0, 0

    for line in file.readlines():
        
        if "=" in line:
            equation = line.split()[-1].split("=")
            instrcutions.append((equation[0], int(equation[1])))

        elif "," in line:
            point = line.strip().split(",")

            x, y = int(point[0]), int(point[1])

            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

            points.append((x, y))


# Map Points onto Matrix

matrix = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for point in points:
    x, y = point
    matrix[y][x] = "#"


# Apply Folds

for fold in instrcutions:

    if fold[0] == "y":

        divide = fold[1]

        original = matrix[0:divide]
        copy = matrix[divide + 1:]

        for y, row in enumerate(copy[::-1]):
            for x, value in enumerate(row):

                if value == "#":
                    original[y][x] = "#"

    else:

        divide = fold[1]

        original = [row[0:divide] for row in matrix]
        copy = [row[divide + 1:] for row in matrix]

        for y, row in enumerate(copy):
            for x, value in enumerate(row[::-1]):

                if value == "#":
                    original[y][x] = "#"

    matrix = original


for row in matrix:
    print(row)