
# Recieve Input from File

TOTAL_STEPS = 2

with open("input.txt", "r") as file:
    input = file.read().split("\n")
    letters = set()

    polymer = input[0]
    rules = {}

    for line in input[2:]:
        key, _, result = line.split()
        letters.update(set(key))

        rules[key] = result


counts = {l:0 for l in letters}

for letter in polymer:
    counts[letter] += 1


# Define Key Function

def tally_insert(first, second, steps=0):

    if steps >= TOTAL_STEPS:
        return
    
    insertion = rules[first + second]
    counts[insertion] += 1

    tally_insert(first, insertion, steps + 1)
    tally_insert(insertion, second, steps + 1)


# Calculate Insertions

index = 0
while index < len(polymer) - 1:

    first, second = polymer[index], polymer[index + 1]
    tally_insert(first, second)

    index += 1


# Find Most and Least Common, then Total

sorted = sorted(counts.values())

smallest = sorted[0]
largest = sorted[-1]

print(counts)
