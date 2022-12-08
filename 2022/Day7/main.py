from collections import deque, Counter
from bisect import bisect


INPUT = "input.txt"
DIR_PREFIX = "directory_"


### Build File System ###

file_system = {}
name_counter = Counter()
file_total = 0


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
        if " ls" not in line and ".." not in line:
            stripped = line.replace("$ ", "").replace("dir", "").strip()
            output.append(stripped)
    return output


def file_system_builder():
    current_file = None
    while True:
        command = yield
        first, second = parse_command(command)

        if first == "cd":
            name = f"{DIR_PREFIX}{second}"
            key = name + str(get_count(name))
            file_system.setdefault(key, [])
            current_file = key

        elif first.isnumeric():
            global file_total
            file_total += int(first)
            key = second + str(get_count(second))
            file_system[key] = int(first)
            file_system[current_file].append(key)

        else:
            name = f"{DIR_PREFIX}{first}"
            key = name + str(name_counter[name])
            file_system[current_file].append(key)


def flatten_directories():

    for k in file_system.keys():
        if k.startswith(DIR_PREFIX):
            flatten_directory(k)


def parse_command(command):
    try:
        first, second = command.split()
    except ValueError:
        first, second = command, ""
    return first, second


def get_count(name):
    count = name_counter[name]
    name_counter[name] += 1
    return count


def flatten_directory(directory):
    children = deque(file_system[directory][:])
    total = 0

    while children:
        child = children.popleft()
        mapped = file_system[child]

        if isinstance(mapped, int):
            total += mapped
        else:
            children.extend(mapped)

    file_system[directory] = total


### Operations on File System ###

def view_file_system(all_files=True):
    for file, size in file_system.items():
        if all_files or file.startswith(DIR_PREFIX):
            print(
                "{0:20} {1}".format(file, size)
            )


def get_sizes_up_to_threshold(threshold):  # Part 1
    total = 0
    for key, size in file_system.items():
        if key.startswith(DIR_PREFIX) and size <= threshold:
            total += size
    return total


def get_smallest_deletable(disk_space=70000000, needed=30000000):  # Part 2
    root_key = f"{DIR_PREFIX}/0"
    unused = disk_space - file_system[root_key]

    print(file_total)
    print(file_system[root_key])

    sizes = sorted(v for k, v in file_system.items() if k.startswith(DIR_PREFIX))
    index = bisect(sizes, needed - unused)

    return sizes[index]


if __name__ == "__main__":
    build_file_system(INPUT)
    view_file_system()
    print(get_smallest_deletable())
