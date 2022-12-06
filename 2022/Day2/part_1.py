
INPUT = "input.txt"

WINNING = {"AY", "BZ", "CX"}
DRAW = {"AX", "BY", "CZ"}

POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def build_matches(path_in):
    matches = []

    with open(path_in) as file_in:
        for line in file_in.readlines():
            match = tuple(line.strip().split(" "))
            matches.append(match)

    return matches


def calculate_match_score(match):
    foreign, local = match
    outcome = foreign + local
    score = POINTS[local]

    if outcome in DRAW:
        score += 3
    elif outcome in WINNING:
        score += 6

    return score


def calculate_total_score(matches):
    return sum(calculate_match_score(m) for m in matches)


if __name__ == "__main__":
    strategy = build_matches(INPUT)
    total = calculate_total_score(strategy)
    print(total)
