fname = "day06_input.txt"
orbits = {}
with open(fname) as fh:
    for line in fh:
        center, obiter  = line.strip().split(")")
        orbits[obiter] = center

total = 0
for item in orbits.keys():
    while item in orbits:
        total += 1
        item = orbits[item]
print("Total orbits:", total)
