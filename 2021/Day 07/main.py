
# Recieve input from file

with open("input.txt", "r") as file:
    input = [int(x) for x in file.read().split(",")]


# Find largest number in input

max = 0
for num in input:
    if num > max:
        max = num


# Find cheapest position (Part 1)

fuel_costs = []

i = 0
while i < max:
    fuel = sum([abs(x - i) for x in input])
    fuel_costs.append(fuel)

    i += 1

cheapest = -1
for cost in fuel_costs:
    if cost < cheapest or cheapest == -1:
        cheapest = cost


# Find cheapest position (Part 1)

fuel_costs = []

i = 0
while i < max:

    triangular = lambda n: ((n**2) + n) / 2
    fuel = sum([triangular(abs(x - i)) for x in input])
    fuel_costs.append(fuel)

    i += 1

cheapest = -1
for cost in fuel_costs:
    if cost < cheapest or cheapest == -1:
        cheapest = cost


print(cheapest)
