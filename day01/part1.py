with open('./day01a_input.txt') as fh:
    fuel = 0
    for line in fh:
        mass = int(line)
        fuel += (mass // 3) - 2
print("fuel requirement:", fuel)
