from itertools import product


INPUT = "input.txt"

MOVES = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def build_moves(path_in):
    moves = []
    with open(path_in, "r") as file:
        for line in file.readlines():
            key, distance = line.strip().split()
            moves.append((key, int(distance)))
    return moves


def move_ends(positions, move):
    occupied = set()
    (hx, hy), (tx, ty) = positions
    key, distance = move

    dx, dy = MOVES[key]
    for _ in range(distance):
        # view_board(
        #    ((hx, hy), (tx, ty))
        # )
        ohx, ohy = hx, hy
        hx += dx
        hy += dy

        if abs(hx - tx) > abs(hy - ty) and abs(hx - tx) > 1 or abs(hy - ty) > abs(hx - tx) and abs(hy - ty) > 1:
            tx, ty = ohx, ohy
        elif abs(hx - tx) > 1 or abs(hy - ty) > 1:
            tx += dx
            ty += dy

        occupied.add((tx, ty))

    return (hx, hy), (tx, ty), occupied


def get_all_tail_positions(moves):
    hx, hy = 0, 0
    tx, ty = 0, 0
    tail_positions = {(tx, ty)}

    for move in moves:
        (hx, hy), (tx, ty), occupied = move_ends(
            ((hx, hy), (tx, ty)), move
        )
        tail_positions.update(occupied)
    return tail_positions


def view_board(positions, width=6, height=5):
    (hx, hy), (tx, ty) = positions
    printed = ""

    print("=" * width)
    for y in range(height):
        for x in range(width):
            if x == hx and y == hy:
                printed += "H"
            elif x == tx and y == ty:
                printed += "T"
            else:
                printed += "."
        printed += "\n"
    print(printed, "\n")


if __name__ == "__main__":
    m = build_moves(INPUT)
    print(
        len(sorted(get_all_tail_positions(m)))
    )
