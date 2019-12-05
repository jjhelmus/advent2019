
def make_path(dir_strs):
    x = y = 0
    path = []
    for dir_str in dir_strs:
        heading = dir_str[0]
        length = int(dir_str[1:])
        if heading == 'U':
            leg = [(x, y+i) for i in range(length)]
            y += length
        if heading == 'D':
            leg = [(x, y-i) for i in range(length)]
            y -= length
        if heading == 'R':
            leg = [(x+i, y) for i in range(length)]
            x += length
        if heading == 'L':
            leg = [(x-i, y) for i in range(length)]
            x -= length
        path.extend(leg)
    return path


with open('./day03_input.txt') as f:
    w1_dirs = f.readline().strip().split(',')
    w2_dirs = f.readline().strip().split(',')

w1_path = make_path(w1_dirs)
w2_path = make_path(w2_dirs)

crossings = set(w1_path).intersection(set(w2_path))
crossings.remove((0, 0))  # we do not care about central port
dist_to_closest = min(i+j for i, j in crossings)
print("Minimum distance:", dist_to_closest)

min_steps = min(w1_path.index(n) + w2_path.index(n) for n in crossings)
print("Minimum steps:", min_steps)
