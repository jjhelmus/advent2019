with open('./day02_input.txt') as fh:
    text = fh.read()
program = [int(i) for i in text.split(',')]

program[1] = 12
program[2] = 2

position = 0
while True:
    op = program[position]
    if op == 99:
        break
    p1 = program[position+1]
    p2 = program[position+2]
    p3 = program[position+3]
    v1 = program[p1]
    v2 = program[p2]
    if op == 1:
        program[p3] = v1 + v2
    elif op == 2:
        program[p3] = v1 * v2
    else:
        raise ValueError(op)
    position += 4

print("position 0 is:", program[0])

