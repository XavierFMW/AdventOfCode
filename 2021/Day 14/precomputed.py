
# Recieve Input from File

TOTAL_STEPS = 40
PRECOMPUTED_STEPS = 20

INTERNAL_STEPS = TOTAL_STEPS // PRECOMPUTED_STEPS

with open("input.txt", "r") as file:
    input = file.read().split("\n")
    letters = set()

    polymer = input[0]
    rules = {}

    for line in input[2:]:
        key, _, result = line.split()
        letters.update(set(key))

        rules[key] = result

outputs = {}
total_counter = {l:0 for l in letters}

for letter in polymer:
    total_counter[letter] += 1


# Define Key Function

def tally_inserts(first, second, counter, result, steps=0):
    
    insertion = rules[first + second]
    
    if steps >= PRECOMPUTED_STEPS:
        result.extend([first + insertion, insertion + second])
        return

    counter[insertion] += 1

    tally_inserts(first, insertion, counter, result, steps + 1)
    tally_inserts(insertion, second, counter, result, steps + 1)


def tally_outputs(starting_pair, steps=0):

    if steps >= INTERNAL_STEPS:
        return

    print(steps)

    tally, result = outputs[starting_pair]

    for letter in tally:
        total_counter[letter] += tally[letter]

    for pair in result:
        tally_outputs(pair, steps + 1)


# Precompute Output per Pair

for pair in rules:

    first, second = pair[0], pair[1]

    counter = {l:0 for l in letters}
    result = []

    tally_inserts(first, second, counter, result)
    outputs[pair] = (counter, result)


# Calculate Insertions

index = 0
while index < len(polymer) - 1:
    
    pair = polymer[index] + polymer[index + 1]
    tally_outputs(pair)

    index += 1


# Find Most and Least Common, then Total

sorted = sorted(total_counter.values())

smallest = sorted[0]
largest = sorted[-1]

print(total_counter)
