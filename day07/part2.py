from itertools import permutations

from intcode import IntCodeComputer

def looped_amps(memory_str, phases):
    amps = [IntCodeComputer(memory_str) for _ in range(5)]
    signal = 0
    first = True
    while True:
        for amp, phase in zip(amps, phases):
            if first:
                input_ = (phase, signal)
            else:
                input_ = (signal, )
            output = amp.run(input_)
            if output is None:
                return signal
            signal = output
        first = False

with open("./day07_input.txt") as fh:
    memory_str = fh.read()
options = (5, 6, 7, 8, 9)
signals = {p: looped_amps(memory_str, p) for p in permutations(options, 5)}
print("Part 2:", max(signals.values()))
