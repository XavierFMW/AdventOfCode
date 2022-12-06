
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Run Program

increases = 0
index = 0

while index + 3 <= len(input) - 1:

    first_sum = int(input[index]) + int(input[index + 1]) + int(input[index + 2])
    second_sum = int(input[index + 1]) + int(input[index + 2]) + int(input[index + 3])

    if second_sum > first_sum:
        increases += 1

    index += 1

print(f"\n{increases}")