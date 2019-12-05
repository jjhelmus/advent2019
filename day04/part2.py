from collections import Counter
password_min = 125730
password_max = 579381
valid_passwords = 0
for password in range(password_min, password_max):
    digits = tuple(int(c) for c in str(password))
    decreasing = all(i <= j for i, j in zip(digits[:-1], digits[1:]))
    if not decreasing:
        continue
    # this also checks for repeat digits
    digit_count = Counter(digits)
    repeat_two = 2 in digit_count.values()
    if repeat_two:
        valid_passwords += 1
print("Number of valid passwords:", valid_passwords)
