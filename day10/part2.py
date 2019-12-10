import math

def read(fname):
    locations = []
    with open(fname) as fh:
        for i, line in enumerate(fh):
            for j, char in enumerate(line):
                if char == "#":
                    locations.append((j, i))
    return locations

def get_angle(astroid, station):
    x1, y1 = astroid
    x2, y2 = station
    y = y2 - y1
    x = x2 - x1
    return math.atan2(-x, y)

def get_dist(astroid, station):
    x1, y1 = astroid
    x2, y2 = station
    y = y2 - y1
    x = x2 - x1
    return x*x + y*y

def get_angles(field, station):
    return [get_angle(a, station) for a in field if a != station]

def get_dists(field, station):
    return [get_dist(a, station) for a in field if a != station]

def find_max_station(locations):
    viz = {s: len(set(get_angles(locations, s))) for s in locations}
    return max(viz, key=viz.get)

def order_angle(angle):
    if angle >= 0:
        return angle-8
    else:
        return angle

fname = "./day10_input.txt"
locations = read(fname)
station = find_max_station(locations)
print("Station:", station)
locations.pop(locations.index(station))

angles = get_angles(locations, station)
dist = get_dists(locations, station)
adj_angles = [order_angle(i) for i in angles]
lookup = {(d, a): loc for d, a, loc in zip(dist, adj_angles, locations)}
for i, adj_angle in enumerate(sorted(set(adj_angles))):
    min_dist = min(d for d, a in zip(dist, adj_angles) if a == adj_angle)
    station = lookup[(min_dist, adj_angle)]
    if i == 199:
        print(f"{i+1}: {station}")  # 14, 17
