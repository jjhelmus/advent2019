from itertools import permutations
from intcode import IntCodeComputer

def run_amps(memory_str, phases):
    signal = 0
    for phase in phases:
        signal = IntCodeComputer(memory_str).run(input_=[phase, signal])
    return signal

with open("./day07_input.txt") as fh:
    memory_str = fh.read()
options = range(5)
signals = {p: run_amps(memory_str, p) for p in permutations(options, 5)}
print("Part 1:", max(signals.values()))
