
INPUT = "input.txt"

WINNING = {
    "A": "B",
    "B": "C",
    "C": "A",
}

LOSING = {
    "A": "C",
    "B": "A",
    "C": "B",
}

POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def build_matches(path_in):
    matches = []

    with open(path_in) as file_in:
        for line in file_in.readlines():
            match = tuple(line.strip().split(" "))
            matches.append(match)

    return matches


def calculate_match_score(match):
    hand, outcome = match

    if outcome == "X":
        play = LOSING[hand]
        return POINTS[play]
    elif outcome == "Y":
        return POINTS[hand] + 3
    else:
        play = WINNING[hand]
        return POINTS[play] + 6


def calculate_total_score(matches):
    return sum(calculate_match_score(m) for m in matches)


if __name__ == "__main__":
    strategy = build_matches(INPUT)
    total = calculate_total_score(strategy)
    print(total)
