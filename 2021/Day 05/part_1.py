
# Analyze input from file

max_x, max_y = 0, 0

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):

        line_points = []
        points = line.replace("\n", "").replace(" ", "").split("->")

        for point in points:

            unprocessed = point.split(",")
            x, y = int(unprocessed[0]), int(unprocessed[1])

            if x > max_x:
                max_x = x

            if y > max_y:
                max_y = y

            line_points.append((x, y))

        input[index] = line_points

matrix = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]


# Define key functions

def print_board(matrix):

    for row in matrix:
        print(row)

    print("\n")


# Plot lines on matrix

for line in input:

    start_point = line[0]
    end_point = line[1]

    if start_point[1] == end_point[1]:

        x1 = start_point[0]
        x2 = end_point[0]
        y = start_point[1]

        if x1 < x2:
            smallest_x = x1
            largest_x = x2
        else:
            smallest_x = x2
            largest_x = x1

        x = smallest_x
        while x <= largest_x:
            
            if matrix[y][x] == ".":
                matrix[y][x] = 1
            else:
                matrix[y][x] += 1

            x += 1

    elif start_point[0] == end_point[0]:
        
        y1 = start_point[1]
        y2 = end_point[1]
        x = start_point[0]

        if y1 < y2:
            smallest_y = y1
            largest_y = y2
        else:
            smallest_y = y2
            largest_y = y1

        y = smallest_y
        while y <= largest_y:
            
            if matrix[y][x] == ".":
                matrix[y][x] = 1
            else:
                matrix[y][x] += 1

            y += 1

    else:

        if start_point[1] > end_point[1]:
            top = start_point
            bottom = end_point
        else:
            top = end_point
            bottom = start_point

        x1, x2 = top[0], bottom[0]
        y1, y2 = top[1], bottom[1]

        if x2 > x1:
            increasing = True
        else:
            increasing = False

        x, y = x1, y1
        while y >= y2:

            if matrix[y][x] == ".":
                matrix[y][x] = 1
            else:
                matrix[y][x] += 1
        
            y -= 1

            if increasing:
                x += 1
            else:
                x -= 1


# Analyze points of matrix

dangerous_points = [point for row in matrix for point in row if isinstance(point, int) and point > 1]
dangerous = len(dangerous_points)

print(dangerous)
