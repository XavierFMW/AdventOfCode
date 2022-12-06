from collections import Counter
from time import process_time

# Receive Input from File

with open("input.txt", "r") as file:

    matrix = []
    for line in file.readlines():
        matrix.append([int(x) for x in line.strip()])


NODES = []
TILES_ADDED = 5


# Define Functions

def increment_matrix(matrix):

    copied = matrix.copy()

    for y, row in enumerate(copied):
        for x, _ in enumerate(row):
            copied[y][x] += 1
            if copied[y][x] > 9:
                copied[y][x] = 1

    return copied


# Expand Matrix

row = [row.copy() for row in matrix]
expanded = []

incremented = increment_matrix(matrix)
for _ in range(TILES_ADDED - 1):

    for step in range(len(matrix)):
        row[step].extend(incremented[step])

    incremented = increment_matrix(incremented)

for _ in range(TILES_ADDED):
    expanded.extend([r.copy() for r in row])
    row = increment_matrix(row)

matrix = expanded
SIZE = len(matrix) - 1
TARGET = (SIZE, SIZE)



# Define Node Class

class node:

    def __init__(self, point):

        x, y = point
        self.point = point
        self.value = matrix[y][x]

        self.heuristic = abs(x - TARGET[0]) + abs(y - TARGET[1])    # Distance from target
        self.distance = None    # Distance from starting node
        self.total = None    # Total cost

        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        self.neighbors = [n for n in NODES if n.point in adjacent]

        for n in self.neighbors:
            n.neighbors.append(self)

        NODES.append(self)

    
    def update_distance(self, new):

        self.distance = new
        self.total = new + self.heuristic


# Build Matrix of Nodes

for y in range(SIZE + 1):
    for x in range(SIZE + 1):
        
        t = process_time()
        node((x, y))

        print(x, y, process_time() - t)


# Begin Pathfinding

END_COST = None
OPEN = []
CLOSED = []

ROOT = NODES[0]
ROOT.update_distance(0)
OPEN.append(ROOT)

while END_COST == None:

    c = Counter({n:n.distance for n in OPEN if n.distance != None})
    nodes_by_cost = list(c.most_common())
        
    current, _ = nodes_by_cost[-1]
    x, y = current.point
    matrix[y][x] = "#"

    print(current.point)

    OPEN.remove(current)
    CLOSED.append(current)

    if current.point == TARGET:
        END_COST = current.distance
        break

    for neighbor in current.neighbors:

        if neighbor in CLOSED:
            continue

        cost = neighbor.value + current.distance
        if neighbor not in OPEN or neighbor.distance != None and cost < neighbor.distance:
            neighbor.update_distance(cost)

            if neighbor not in OPEN:
                OPEN.append(neighbor)

print(END_COST)
