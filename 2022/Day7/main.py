
INPUT = "input.txt"


### Build File System ###

file_tree = {}


def build_file_tree(path_in):

    with open(path_in, "r") as input_file:
        commands = format_commands(input_file.readlines())

        builder = file_tree_builder()
        next(builder)  # Priming coroutine

        for command in commands:
            builder.send(command)


def format_commands(lines):
    output = []
    for line in lines:
        if "ls" not in line and ".." not in line:
            stripped = line.replace("$ ", "").replace("dir", "").strip()
            output.append(stripped)
    return output


def file_tree_builder():
    current_file = None
    while True:
        command = yield
        first, second = parse_command(command)

        if first == "cd":
            key = f"directory_{second}"
            file_tree[key] = []
            current_file = key

        elif first.isnumeric():
            file_tree[second] = int(first)
            file_tree[current_file].append(second)

        else:
            key = f"directory_{first}"
            file_tree[current_file].append(key)


def parse_command(command):
    try:
        first, second = command.split()
    except ValueError:
        first, second = command, ""
    return first, second


### Operations on File System ###

def get_size(key):
    size = 0
    mapped = file_tree[key]

    if isinstance(mapped, int):
        size += mapped

    else:
        for item in mapped:
            size += get_size(item)

    return size


def get_sizes_up_to_threshold(threshold):
    total = 0
    for key in file_tree.keys():
        size = get_size(key)
        if size <= threshold:
            total += size
    return total


if __name__ == "__main__":
    build_file_tree(INPUT)
    for key in file_tree.keys():
        print(
            key, get_size(key)
        )
