
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Run Program

x, y, angle = 0, 0, 0

for line in input:

    command = line.split(" ")[0]
    num = int(line.split(" ")[1])

    if command == "forward":

        x += num
        y += num * angle
        
    elif command == "down":
        angle += num

    elif command == "up":
        angle -= num

total = x * y
print(total)
