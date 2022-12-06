

# Recieve input from file

with open("input.txt", "r") as file:

    displays = []
    for line in file.readlines():
        
        signals, output = line.split("|")

        signals = signals.split()
        output = output.split()

        displays.append((signals, output))


# I'm so tired I don't even know what to title this section. "do math" I guess.

total_output = 0
for display in displays:

    signals = sorted(display[0], key=len)
    outputs = display[1]

    digits = {
        "1": "".join(sorted(signals[0])),
        "7": "".join(sorted(signals[1])),
        "4": "".join(sorted(signals[2])),
        "8": "".join(sorted(signals[9])),
        }

    for signal in [x for x in signals if len(x) == 5]:

        matching = len([_ for _ in signal if _ in digits["4"]]) + len([_ for _ in signal if _ in digits["1"]])

        if matching == 5:
            digits["3"] = "".join(sorted(signal))
        elif matching == 4:
            digits["5"] = "".join(sorted(signal))
        else:
            digits["2"] = "".join(sorted(signal))

    for signal in [x for x in signals if len(x) == 6]:

        matching = len([_ for _ in signal if _ in digits["3"]]) + len([_ for _ in signal if _ in digits["5"]])

        if matching == 10:
            digits["9"] = "".join(sorted(signal))
        elif matching == 9:
            digits["6"] = "".join(sorted(signal))
        else:
            digits["0"] = "".join(sorted(signal))
    
    translator = {value:key for key, value in digits.items()}
    translated_output = ""

    for output in outputs:
        output = "".join(sorted(output))
        translated_output += translator[output]

    total_output += int(translated_output)


print(total_output)
