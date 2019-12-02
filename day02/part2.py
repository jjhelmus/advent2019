def run_program(memory):
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        if opcode == 99:
            break
        parameter1 = memory[instruction_pointer+1]
        parameter2 = memory[instruction_pointer+2]
        parameter3 = memory[instruction_pointer+3]
        v1 = memory[parameter1]
        v2 = memory[parameter2]
        if opcode == 1:
            memory[parameter3] = v1 + v2
        elif opcode == 2:
            memory[parameter3] = v1 * v2
        else:
            raise ValueError(
                f"Invalid opcode {opcode} as address {instruction_pointer}")
        instruction_pointer += 4
    return


with open('./day02_input.txt') as fh:
    text = fh.read()
original_memory = [int(i) for i in text.split(',')]

for noun in range(100):
    for verb in range(100):
        memory = original_memory.copy()
        memory[1] = noun
        memory[2] = verb
        try:
            run_program(memory)
        except:
            continue
        if memory[0] == 19690720:
            print(f"noun: {noun}, verb {verb}")
            print("answer:", 100 * noun + verb)
