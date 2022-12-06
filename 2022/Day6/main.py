from collections import deque


INPUT = "input.txt"


def get_input(path_in):
    with open(path_in, "r") as file:
        return file.read().strip()


def find_marker_position(text, size):
    previous = deque(c for c in text[:size])
    indexed = size

    for char in text[size:]:
        if not are_duplicates(previous):
            return indexed
        previous.popleft()
        previous.append(char)
        indexed += 1


def are_duplicates(collection):
    seen = set(collection)
    return len(collection) != len(seen)


if __name__ == "__main__":
    signal = get_input(INPUT)
    position = find_marker_position(signal, size=14)  # Set size to 4 for part one, 14 for part 2.
    print(position)
