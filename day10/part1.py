import math

def read(fname):
    locations = []
    with open(fname) as fh:
        for i, line in enumerate(fh):
            for j, char in enumerate(line):
                if char == "#":
                    locations.append((i, j))
    return locations

def get_angle(astroid, station):
    x1, y1 = astroid
    x2, y2 = station
    y = y2 - y1
    x = x2 - x1
    return math.atan2(y, x)

def get_angles(field, station):
    return [get_angle(station, a) for a in field if a != station]

def find_max_viz(fname):
    locations = read(fname)
    viz = [len(set(get_angles(locations, s))) for s in locations]
    return max(viz)

print(find_max_viz('example1.txt'))
print(find_max_viz('example2.txt'))
print(find_max_viz('example3.txt'))
print(find_max_viz('./day10_input.txt'))
