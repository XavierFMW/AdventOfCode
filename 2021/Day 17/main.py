from math import ceil


# Set Target Bounds

X_MIN, X_MAX = 287, 309
Y_MIN, Y_MAX = -76, -48

"""
X_MIN, X_MAX = 20, 30
Y_MIN, Y_MAX = -10, -5
"""

X_RANGE, Y_RANGE = X_MAX * 2, abs(Y_MIN) * 2


# Define Pathfinding Function

def hits_target(initial):

    x, y = 0, 0
    xv, yv = initial
    peak_y = 0

    while x <= X_MAX and y >= Y_MIN:

        if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX:
            return True

        x += xv
        y += yv

        if y > peak_y:
            peak_y = y

        if xv > 0:
            xv -= 1

        yv -= 1

    return False

# Calculate Paths

paths = []

for x in range(X_RANGE):
    for y in range(Y_RANGE):
        
        if hits_target((x, y)):
            paths.append((x, y))

        if hits_target((x, -y)):
            paths.append((x, 0 - y))

print(len(set(paths)))

