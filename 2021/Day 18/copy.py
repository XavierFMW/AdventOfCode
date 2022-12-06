from math import ceil


# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Define Node Class

class node:

    def __init__(self, input, depth=0, parent=None):

        starting = input[:]

        if depth == 0:
            self.remaining = input.split(",")
            self.initial = len(self.remaining)
            self.parent = self
        else:
            self.initial = parent.initial
            self.remaining = parent.remaining
            self.parent = parent
        

        if input[1] != "[":
            self.left = int(input[1])
            input = ",".join(input.split(",")[1:])
        
        else:
            self.left = node(input[1:], depth + 1, self.parent)

            if depth == 0:
                input = ",".join(self.remaining)

            else:
                separated = input.split(",")
                divider = self.initial // (depth * 2)
                
                input = ",".join(separated[divider:])


        print(f"{starting}  |  {input}  |  {depth}")
        if input[0] != "[":
            self.right = int(input[0])
        else:
            self.right = node(input, depth + 1, self.parent)

        if len(input.split(",")) <= len(self.parent.remaining):
            self.parent.remaining = input.split(",")[1:]


# Convert Input to Tree


node(input[0])