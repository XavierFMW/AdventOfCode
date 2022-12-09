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


def move_segments(moves, segments=2):
    tail_occupied = set()
    rope = tuple([0, 0] for _ in range(segments))
    head = rope[0]

    for move in moves:
        key, distance = move
        dx, dy = MOVES[key]

        for _ in range(distance):
            view_board(rope)
            ohx, ohy = head
            head[0] += dx
            head[1] += dy
            for index in range(1, segments):
                leader = rope[index - 1]
                follower = rope[index]
                hx, hy = leader
                tx, ty = follower
                if abs(hx - tx) > abs(hy - ty) and abs(hx - tx) > 1:
                    follower[0] = hx
                    follower[1] = hy + (ty - hy)
                elif abs(hy - ty) > abs(hx - tx) and abs(hy - ty) > 1:
                    follower[0] = hx + (tx - hx)
                    follower[1] = hy
                elif abs(hx - tx) > 1 or abs(hy - ty) > 1:
                    follower[0] += dx
                    follower[1] += dy
                ohx, ohy = tx, ty

                if index == segments - 1:
                    tail_occupied.add(tuple(rope[index]))

    return tail_occupied


def view_board(rope, width=6, height=5):
    printed = []

    print("=" * width)
    for y in range(height):
        row = ""
        for x in range(width):
            if [x, y] in rope:
                row += str(rope.index([x, y]))
            else:
                row += "."
        printed.append(row)
    for r in printed[::-1]:
        print(r)
    print("\n")


if __name__ == "__main__":
    m = build_moves(INPUT)
    print(len(move_segments(m, 10)))
