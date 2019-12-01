def fuel_req(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_req(fuel)


# test cases given in problem
assert fuel_req(14) == 2
assert fuel_req(1969) == 966
assert fuel_req(100756) == 50346

with open('./day01a_input.txt') as fh:
    total_fuel = 0
    for line in fh:
        mass = int(line)
        total_fuel += fuel_req(mass)
print("total fuel requirement:", total_fuel)

