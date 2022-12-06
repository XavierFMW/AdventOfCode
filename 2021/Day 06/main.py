
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Analyze input data

colony = []
for line in input:
    colony.extend([int(x) for x in line.split(",")])


# Run population simulations

births = 0
zeros = len([x for x in colony if x == 0])
ones = len([x for x in colony if x == 1])
twos = len([x for x in colony if x == 2])
threes = len([x for x in colony if x == 3])
fours = len([x for x in colony if x == 4])
fives = len([x for x in colony if x == 5])
sixes = len([x for x in colony if x == 6])
sevens = len([x for x in colony if x == 7])
eights = len([x for x in colony if x == 8])


days = 0
while days <= 10000:

    births = zeros
    zeros = ones
    ones = twos
    twos = threes
    threes = fours
    fours = fives
    fives = sixes
    sixes = sevens
    sevens = eights
    eights = 0

    sixes += births
    eights += births

    days += 1

total = zeros + ones + twos + threes + fours + fives + sixes + sevens + eights
print(total)

