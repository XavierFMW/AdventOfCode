

# Recieve input from file

with open("input.txt", "r") as file:
    input = file.read().strip()


# Define Parsing Functions

def hex_to_bin(hex):

    output = ""
    translator = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    for h in hex:
        output = output + translator[h]

    return output


def parse_packet(packet, limit=1000):

    packet = packet[:]
    values = []

    total_length = 0
    packets = 0

    if len(packet) == 0:
        return (0, 0)

    else:
        
        while len([b for b in packet if b != "0"]) > 0 and packets < limit:

            version = int(packet[:3], 2)
            type = int(packet[3:6], 2)

            packet_length = 6
            
            if type == 4:

                data = packet[6:]
                value = ""

                prefix = "1"
                index = 0

                while prefix == "1":

                    prefix = data[index]

                    value = value + data[index + 1:index + 5]
                    index += 5

                value = int(value, 2)
                values.append(value)

                packet_length += index
                total_length += packet_length

                packet = packet[packet_length:]

            else:

                length_id = int(packet[6])
                packet_length = 7

                if length_id == 1:
                    subpackets = int(packet[7:18], 2)
                    sub_values, sub_length = parse_packet(packet[18:], subpackets)

                    packet_length += 11 + sub_length

                else:
                    length = int(packet[7:22], 2) + 22
                    sub_values, sub_length = parse_packet(packet[22:length])

                    packet_length += 15 + sub_length


                if type == 0:
                    total = sum(sub_values)

                elif type == 1:

                    total = 1
                    for n in sub_values:
                        total *= n

                elif type == 2:
                    total = min(sub_values)

                elif type == 3:
                    total = max(sub_values)

                elif type == 5 and sub_values[0] > sub_values[1] or type == 6 and sub_values[0] < sub_values[1] or type == 7 and sub_values[0] == sub_values[1]:
                    total = 1

                else:
                    total = 0
                
                values.append(total)
                total_length += packet_length
                packet = packet[packet_length:]

            packets += 1

        if limit == 1000:
            total_length += len(packet)

        return (values, total_length)



# Parse through Input

bits = hex_to_bin(input)

output_values, input_length = parse_packet(bits)
print(output_values)

