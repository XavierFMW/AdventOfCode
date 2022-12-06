
# Recieve input from file

with open("input.txt", "r") as file:

    displays = []
    for line in file.readlines():
        
        signals, output = line.split("|")

        signals = signals.split()
        output = output.split()

        displays.append((signals, output))


# Count number of unique digits in output

unique_digits = 0
for output in [display[1] for display in displays]:
    unique_digits += len([value for value in output if len(value) in {2, 3, 4, 7}])

print(unique_digits)
