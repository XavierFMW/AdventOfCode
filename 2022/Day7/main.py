
files = {}
INPUT = "input.txt"


def build_file_tree(path_in):

    with open(path_in, "r") as commands:
        lines = format_commands(commands.readlines())


def format_commands(lines):
    output = []
    for line in lines:
        if "ls" not in line and ".." not in line:
            stripped = line.replace("$ ", "").replace("dir", "").strip()
            output.append(stripped)
    return output


# Replace with Generator Coroutine
def builder_factory():
    current_file = None

    def builder(command):
        unzipped = command.split()
        if unzipped[0] == "cd":
            key = unzipped[1]
            current_file = key



if __name__ == "__main__":
    build_file_tree(INPUT)
