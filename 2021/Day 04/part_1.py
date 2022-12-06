
# Recieve input from file

with open("input.txt", "r") as file:
    input = file.readlines()


# Create drawn numbers and boards

drawn_nums = [int(x) for x in input[0].split(",")]
boards = []

line_index = 2
while line_index < len(input) - 2:

    subset = input[line_index: line_index + 5]
    board = []

    for line in subset:
        
        strings = line.replace("\n", "").split(" ")

        row = [int(x) for x in strings if x != ""]
        board.append(row)

    boards.append(board)

    line_index += 6


# Define reuseable functions

def print_board(board):

    for row in board:
        print(row)

    print("\n")

def check_bingo(boards):

    for board in boards:

        index = 0
        while index < len(board[0]):

            row = board[index]
            column = [row[index] for row in board]

            if row == ["X", "X", "X", "X", "X"] or column == ["X", "X", "X", "X", "X"]:
                return board

            index += 1

    return None


# Mark off drawn numbers, check for bingo

winner = None
last_drawn = 0

for drawn in drawn_nums:

    for board in boards:

        for y, row in enumerate(board):
            for x, value in enumerate(row):

                if value == drawn:
                    board[y][x] = "X"

    winner = check_bingo(boards)

    if winner:

        last_drawn = drawn
        break


# Find sum of winning board

unmarked = [value for row in winner for value in row if value != "X"]
score = sum(unmarked) * last_drawn

print(score)
