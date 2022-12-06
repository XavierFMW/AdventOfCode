
# Recieve Input from File

TOTAL_STEPS = 40

with open("input.txt", "r") as file:
    input = file.read().split("\n")

    polymer = input[0]
    rules = {}

    for line in input[2:]:
        key, _, result = line.split()
        rules[key] = result


total_count = {}

index = 0
while index < len(polymer) - 1:
    key = polymer[index] + polymer[index + 1]

    if key in total_count.keys():
        total_count[key] += 1
    else:
        total_count[key] = 1

    index += 1


# Calculate Insertions

initial_pair = polymer[0:2]
for _ in range(TOTAL_STEPS):

    count = {}

    for key in total_count.keys():

        pairs = [key[0] + rules[key], rules[key] + key[1]]
        
        for pair in pairs:

            if pair in count.keys():
                count[pair] += total_count[key] 
            else:
                count[pair] = total_count[key]
    
    initial_pair = list(count.keys())[0]
    total_count = count


# Find Most and Least Common

total_count[initial_pair] -= 1
letter_count = {k[0]: 0 for k in rules.keys()}

for letter in initial_pair:
    letter_count[letter] += 1

for pair in total_count:
    letter_count[pair[-1]] += total_count[pair]

sorted = sorted(list(letter_count.values()))
print(sorted[-1] - sorted[0])
