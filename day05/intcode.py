# instruction opcodes
OPCODE_ADDITION = 1
OPCODE_MULTIPLY = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JUMP_IF_TRUE = 5
OPCODE_JUMP_IF_FALSE = 6
OPCODE_LESS_THAN = 7
OPCODE_EQUAL = 8
OPCODE_HALT = 99

# parameter modes
MODE_POSITION = 0
MODE_IMMEDIATE = 1


class IntCodeComputer(object):

    def __init__(self, memory_str):
        self.memory = [int(i) for i in memory_str.split(",")]

    def run(self, input_=None):
        self.ip = 0
        output = []
        while True:
            opcode, modes = self.decode_instruction()
            if opcode == OPCODE_HALT:
                break
            if opcode == OPCODE_ADDITION:
                p1, p2, p3 = self.decode_nparams(modes, 3, True)
                self.memory[p3] = p1 + p2
            elif opcode == OPCODE_MULTIPLY:
                p1, p2, p3 = self.decode_nparams(modes, 3, True)
                self.memory[p3] = p1 * p2

            elif opcode == OPCODE_INPUT:
                p1, = self.decode_nparams(modes, 1, True)
                self.memory[p1] = input_
            elif opcode == OPCODE_OUTPUT:
                p1, = self.decode_nparams(modes, 1)
                output.append(p1)

            elif opcode == OPCODE_JUMP_IF_TRUE:
                p1, p2 = self.decode_nparams(modes, 2)
                if p1 != 0:
                    self.ip = p2
            elif opcode == OPCODE_JUMP_IF_FALSE:
                p1, p2 = self.decode_nparams(modes, 2)
                if p1 == 0:
                    self.ip = p2
            elif opcode == OPCODE_LESS_THAN:
                p1, p2, p3 = self.decode_nparams(modes, 3, True)
                self.memory[p3] = {True: 1, False: 0}[p1<p2]
            elif opcode == OPCODE_EQUAL:
                p1, p2, p3 = self.decode_nparams(modes, 3, True)
                self.memory[p3] = {True: 1, False: 0}[p1==p2]

            else:
                self.fail(opcode)
        return output

    def decode_instruction(self):
        """ Decode an instruction, return the opcode and parameter modes. """
        instruction = self.memory[self.ip]
        m3, remain = divmod(instruction, 10_000)
        m2, remain = divmod(remain, 1_000)
        m1, opcode = divmod(remain, 100)
        self.ip += 1
        return opcode, (m1, m2, m3)

    def decode_nparams(self, modes, number, last_write=False):
        is_write = [False] * number
        if last_write:
            is_write[-1] = True
        return self.decode_params(modes, is_write)

    def decode_params(self, modes, is_write):
        """ Fetch and decode the parameters depending on mode. """
        number = len(is_write)
        params = self.fetch_parameters(number)
        return tuple(self.get_value(*t) for t in zip(params, modes, is_write))

    def fetch_parameters(self, number):
        """ Fetch raw parameters from memory """
        params = self.memory[self.ip:self.ip+number]
        self.ip += number
        return params

    def get_value(self, parameter, mode, ignore_mode=False):
        """ Decode a parameter according to the mode. """
        if ignore_mode:
            return parameter
        if mode == MODE_IMMEDIATE:
            return parameter
        if mode == MODE_POSITION:
            return self.memory[parameter]
        else:
            self.fail()

    def fail(self, opcode=None):
        raise ValueError(f"Failure: opcode {opcode}, ip: {self.ip}")
