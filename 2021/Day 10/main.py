
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()

    for index, line in enumerate(input):
        input[index] = line.replace("\n", "")


# Define constant values

OPENING = "([{<"
CLOSING = {"(": ")", "[": "]", "{": "}", "<": ">"}


# Define key functions

def match(following):

    partner = None
    unpaired = 0

    for symbol in following:

        if symbol in OPENING:
            unpaired += 1
        else:
            unpaired -= 1

        if unpaired == -1:

            partner = symbol
            break

    return partner


# Find score for corrupted files

error_score = 0
corrupted = []

for line in input:

    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegal = None

    index = 0
    while index < len(line) and illegal == None:

        character = line[index]
        if character in OPENING:

            following = line[index + 1:]
            partner = match(following)

            if partner and partner != CLOSING[character]:
                corrupted.append(line)
                illegal = partner
        
        index += 1


    if illegal:
        error_score += scores[illegal]


# Find score for incomplete

completion_scores = []
for line in [x for x in input if x not in corrupted]:
    
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    completed = ""

    line_score = 0

    for index, character in enumerate(line):

        following = line[index + 1:]
        if character in OPENING and match(following) == None:
            completed = CLOSING[character] + completed

    
    for closer in completed:
        line_score *= 5
        line_score += scores[closer]
    
    completion_scores.append(line_score)


completion_scores.sort()
size = len(completion_scores)

middle_score = completion_scores[(size // 2)]
