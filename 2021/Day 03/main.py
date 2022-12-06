
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Define a necessary function

def most_common_bit(list):

    zeros = 0
    ones = 0

    for bit in list:

        if bit == 1:
            ones += 1
        else:
            zeros += 1

    if ones > zeros:
        return "1"
    elif zeros > ones:
        return "0"
    else:
        None


# Alayze the input data

matrix = []

for line in input:

    binary = []

    for bit in line:
        binary.append(int(bit))

    matrix.append(binary)

size = len(matrix[0])


# Solve Part 1

gamma = ""
epsilon = ""

column = 0
while column < size:

    swap_bit = {"0": "1", "1": "0"}
    bits_input = [row[column] for row in matrix]

    most_common = most_common_bit(bits_input)
    least_common = swap_bit[most_common]

    gamma = gamma + most_common
    epsilon = epsilon + least_common

    column += 1

print(gamma, epsilon)
# Convert gamma and epsilon to decimal using an external source. Multiply with calculator.


# Solve Part 2

O2_matrix = matrix.copy()

column = 0
while column < size and len(O2_matrix) > 1:

    bits_input = [row[column] for row in O2_matrix]
    most_common = most_common_bit(bits_input)

    if most_common:
        most_common = int(most_common)
    else:
        most_common = 1

    O2_matrix = [row for row in O2_matrix if row[column] == most_common]

    column += 1

O2 = O2_matrix[0]


CO2_matrix = matrix.copy()

column = 0
while column < size and len(CO2_matrix) > 1:

    swap_bit = {"0": 1, "1": 0, None: 0}

    bits_input = [row[column] for row in CO2_matrix]
    least_common = swap_bit[most_common_bit(bits_input)]

    CO2_matrix = [row for row in CO2_matrix if row[column] == least_common]

    column += 1

CO2 = CO2_matrix[0]

print(O2, CO2)
# Once again, convert both binary values to decimal using an external source, then multiply using a calculator.

