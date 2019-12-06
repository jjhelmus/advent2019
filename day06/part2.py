def find_path(start, orbits):
    path = [start]
    while path[-1] in orbits:
        path.append(orbits[path[-1]])
    return path

#fname = "sample2.txt"
fname = "day06_input.txt"
orbits = {}
with open(fname) as fh:
    for line in fh:
        center, obiter  = line.strip().split(")")
        orbits[obiter] = center

you_path = find_path("YOU", orbits)
san_path = find_path("SAN", orbits)
for i in you_path:
    if i in san_path:
        first_shared = i
        break
you_to_shared = you_path.index(first_shared)
san_to_shared = san_path.index(first_shared)
print("Orbital transfers:", you_to_shared + san_to_shared - 2)
