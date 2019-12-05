from intcode import IntCodeComputer

with open('./day05_input.txt') as fh:
    memory_str = fh.read()

computer = IntCodeComputer(memory_str)
output = computer.run(input_=1)
print("Part One:", output[-1])
assert output[-1] == 7265618

computer = IntCodeComputer(memory_str)
output = computer.run(input_=5)
print("Part Two:", output[-1])
assert output[-1] == 7731427
