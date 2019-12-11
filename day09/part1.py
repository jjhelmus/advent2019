
from intcode import IntCodeComputer

with open("./day09_input.txt") as fh:
    memory_str = fh.read()
input_ = [0]

#memory_str = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
#memory_str = "1102,34915192,34915192,7,4,7,99,0"
#memory_str = "104,1125899906842624,99"
#input_=None
computer = IntCodeComputer(memory_str)
output = computer.run(input_=input_)
print(output)
while output is not None:
    output = computer.run()
    print(output)
