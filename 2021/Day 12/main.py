
# Recieve Input from File

from os import path


with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.strip()


# Define Node Class

class node:

    def __init__(self, name):
        
        self.name = name
        self.connections = []


# Define Key Function

def small_cave_doubled(path):

    path = path.split(",")
    small_caves = [x for x in nodes if x.name == x.name.lower()]

    for cave in small_caves:

        if len([x for x in path if x == cave.name]) > 1:
            return True
    
    return False


def find_paths_to(start, end, path=""):

    if start == start.lower():

        if start in path.split(",") and small_cave_doubled(path) or start == "start" and path != "":
            return []

    if path == "":
        path = start
    else:
        path = path + f",{start}"


    if start == end:
        return [path]

    else:

        total_paths = []

        parent = [n for n in nodes if n.name == start][0]
        for n in parent.connections:
            total_paths.extend(find_paths_to(n.name, end, path))

        return total_paths


# Build Map of Nodes

nodes = []
for line in input:

    parent_name, child_name = line.split("-")

    if parent_name in [n.name for n in nodes]:
        parent = [n for n in nodes if n.name == parent_name][0]
    else:
        parent = node(parent_name)
        nodes.append(parent)

    if child_name in [n.name for n in nodes]:
        child = [n for n in nodes if n.name == child_name][0]
    else:
        child = node(child_name)
        nodes.append(child)

    parent.connections.append(child)
    child.connections.append(parent)


paths = find_paths_to("start", "end")
print(len(paths))
    