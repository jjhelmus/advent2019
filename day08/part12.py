from collections import Counter

with open("./day08_input.txt") as fh:
    text = fh.read()
digits = [int(i) for i in text.strip()]

width = 25
tall = 6
per_layer = width * tall

layers = [digits[i:i+per_layer] for i in range(0, len(digits), per_layer)]
digit_counts = [Counter(layer) for layer in layers]
min_counts = min(digit_counts, key=lambda c: c[0])
print("Part 1:", min_counts[1] * min_counts[2])

image = [2] * per_layer
for layer in layers:
    image = [i if j == 2 else j for i, j in zip(layer, image)]

print("Part 2:")
black_square = "\u2588"
for i in range(0, per_layer, width):
    row = image[i:i+width]
    print(''.join([black_square if p else " " for p in row]))
