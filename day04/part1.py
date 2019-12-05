password_min = 125730
password_max = 579381
valid_passwords = 0
for password in range(password_min, password_max):
    digits = tuple(int(c) for c in str(password))
    has_double = len(set(digits)) < 6
    decreasing = all(i <= j for i, j in zip(digits[:-1], digits[1:]))
    if has_double and decreasing:
        valid_passwords += 1
print("Number of valid passwords:", valid_passwords)
