from collections import deque, Counter
from bisect import bisect


INPUT = "input.txt"


### Build File System ###

file_system = {}
directories = set()


def build_file_system(path_in):

    with open(path_in, "r") as input_file:
        commands = format_commands(input_file.readlines())

        builder = file_system_builder()
        next(builder)  # Priming coroutine

        for command in commands:
            builder.send(command)

        flatten_directories()


def format_commands(lines):
    output = []
    for line in lines:
        if " ls" not in line:
            stripped = line.replace("$ ", "").replace("dir", "").strip()
            output.append(stripped)
    return output


def file_system_builder():
    current_path = deque()
    current_directory = []
    while True:
        command = yield
        first, second = parse_command(command)

        if second == "..":
            current_path.pop()

        elif first == "cd":
            file = second
            current_path.append(file)
            key = tuple(current_path)
            file_system.setdefault(key, [])
            directories.add(key)

        elif first.isnumeric():
            size, file = first, second
            current_directory.append(file)
            key = (*current_path, file)
            file_system[key] = int(size)

        else:
            file = first
            current_directory.append(file)

        path_key = tuple(current_path)
        current_directory = file_system[path_key]


def flatten_directories():

    by_depth = sorted(file_system.keys(), key=len)
    for file in by_depth[::-1]:
        file_system[file] = get_size(file)


def parse_command(command):
    try:
        first, second = command.split()
    except ValueError:
        first, second = command, ""
    return first, second


def get_size(file):
    mapped = file_system[file]

    if isinstance(mapped, int):
        return mapped
    else:
        total = 0
        for item in mapped:
            key = (*file, item)
            total += get_size(key)
        return total


### Operations on File System ###

def view_file_system(only_directories=False, spacing=20):

    for file, size in file_system.items():
        if not only_directories or file in directories:
            printable = "/".join(file)
            spaced = "{0:" + str(spacing) + "} {1}"
            print(
                spaced.format(printable, size)
            )


def get_sizes_up_to_threshold(threshold):  # Part 1
    total = 0
    for key, size in file_system.items():
        if key in directories and size <= threshold:
            total += size
    return total


def get_smallest_deletable(disk_space=70000000, needed=30000000):  # Part 2
    root_key = ("/",)
    unused = disk_space - file_system[root_key]

    sizes = sorted(v for k, v in file_system.items() if k in directories)
    index = bisect(sizes, needed - unused)

    return sizes[index]


if __name__ == "__main__":
    build_file_system(INPUT)
