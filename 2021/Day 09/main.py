
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    matrix = []
    for line in input:
        matrix.append([int(x) for x in line.strip()])


# Define necessary function

def point_in_basin(x, y, basin):

    if x < 0 or y < 0 or (x, y) in basin:
        return

    try:
        point = matrix[y][x]

        if point == 9:
            return

        else:
            basin.append((x, y))

            positions = ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))

            for pos in positions:
                point_in_basin(pos[0], pos[1], basin)
    
    except IndexError:
        return


# Find the lowest points in the map

lowest_points = []
for y, row in enumerate(matrix):
    for x, value in enumerate(row):

        points = []
        positions = ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))
        for position in [p for p in positions if p[0] >= 0 and p[1] >= 0]:
            
            pos_x, pos_y = position

            try:
                points.append(matrix[pos_y][pos_x])

            except IndexError:
                pass     
            
            # Yes, I know a try, except, pass block is bad practice. This is the 1/100 times it makes sense to use it.

        if len([x for x in points if x <= value]) == 0:
            lowest_points.append((x, y))


# Calculate the total risk level

total_risk = sum([matrix[point[1]][point[0]] + 1 for point in lowest_points])


# Find basins

basins = []
for point in lowest_points:

    basin = []
    x, y = point

    point_in_basin(x, y, basin)
    basins.append(basin)

basins.sort(key=len)


# Find total from largest basins

total_size = len(basins[-1]) * len(basins[-2]) * len(basins[-3])
print(total_size)
