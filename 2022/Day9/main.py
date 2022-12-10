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


def play_moves(moves, segments=2):
    tails = set()
    rope = [(0, 0) for _ in range(segments)]
    for key, distance in moves:
        for _ in range(distance):
            rope[0] = move_head(rope[0], key)
            for index in range(1, segments):
                follower = rope[index]
                leader = rope[index - 1]
                rope[index] = move_segment(follower, leader)
            tails.add(rope[-1])
    return tails


def move_head(head, key):
    head_x, head_y = head
    delta_x, delta_y = MOVES[key]
    return head_x + delta_x, head_y + delta_y


def move_segment(follower, leader):
    follower_x, follower_y = follower
    leader_x, leader_y = leader
    x_difference = abs(leader_x - follower_x)
    y_difference = abs(leader_y - follower_y)

    if x_difference > y_difference and x_difference > 1:
        x = get_new_coordinate(follower_x, leader_x, x_difference)
        y = leader_y
    elif y_difference > x_difference  and y_difference > 1:
        x = leader_x
        y = get_new_coordinate(follower_y, leader_y, y_difference)
    else:
        x = get_new_coordinate(follower_x, leader_x, x_difference)
        y = get_new_coordinate(follower_y, leader_y, y_difference)

    return x, y


def get_new_coordinate(following, leading, difference):
    new = following
    if difference > 1:
        new += 1 if leading > following else -1
    return new


if __name__ == "__main__":
    m = build_moves(INPUT)
    t_positions = play_moves(m, 10)
    print(len(t_positions))
