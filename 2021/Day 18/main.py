
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Define Node Class

class node:

    def __init__(self, input, depth=0, initial=0):

        if depth == 0:
            initial = len(input.split(","))
        
        if input[1] != "[":
            self.left = int(input[1])
            input = ",".join(input.split(",")[1:])
        
        else:
            self.left = node(input[1:], depth + 1, initial)

            separated = input.split(",")

            if depth == 0:
                divider = initial - 1
            else:
                divider = initial // (depth * 2)

            input = ",".join(separated[divider:])

        if input[0] != "[":
            self.right = int(input[0])
        else:
            self.right = node(input, depth + 1, initial)


# Convert Input to Tree

root = node(input[0])
print(root.left, root.right.left)