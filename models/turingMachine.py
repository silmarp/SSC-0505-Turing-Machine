class Tape():
    default_symbol = "B"

    def __init__(self, string_to_process=""):
        self.__tape = {}
        for i in range(len(string_to_process)):
            self.__tape[i] = string_to_process[i]

    def get_tape_str_representation(self):
        string_representation = ""
        for i in self.__tape.values():
            string_representation += i
        return string_representation

    def get_symbol(self, index):
        if index in self.__tape.keys():
            return self.__tape[index]
        else:
            return self.default_symbol

    def set_symbol(self, index, symbol):
        if index < 0:
            return
        elif index > len(self.get_tape_str_representation()):
            self.__tape.append(symbol)
            return
        self.__tape[index] = symbol


class Instruction():
    def __init__(self, description):
        self.original_state = description[0]
        self.read_symbol = description[2]
        self.next_state = description[4]
        self.write_symbol = description[6]
        self.movement_direction = description[8]


class TuringMachine():
    default_symbol = "B"

    def __init__(self,
                 number_of_states=0,
                 initial_state=0,
                 alphabet=None,
                 extended_alphabet=None,
                 final_state=5,
                 instructions=None,
                 ):
        self.__tape = Tape(string_to_process="")
        self.__head_index = 0
        self.__curent_state = initial_state
        self.__final_state = final_state
        self.__alphabet = alphabet
        self.__extended_alphabet = extended_alphabet
        self.__states = []
        for i in range(number_of_states):
            self.__states.append([])
        for i in instructions:
            self.__states[int(i[0])].append(Instruction(i))

    def set_tape(self, string_to_process=""):
        self.__tape = Tape(string_to_process=string_to_process)

    def is_final_state(self):
        if self.__curent_state == self.__final_state:
            return True
        else:
            return False

    def exec_instuction(self, instuction):
        self.__tape.set_symbol(self.__head_index, instuction.write_symbol)
        if instuction.movement_direction == "R":
            self.__head_index += 1
        else:
            self.__head_index -= 1
        self.__curent_state = int(instuction.next_state)
        return

    def step(self):
        char_under_head = self.__tape.get_symbol(self.__head_index)
        if char_under_head not in self.__extended_alphabet and char_under_head not in self.__alphabet:
            char_under_head = "B"
        for instruction in self.__states[self.__curent_state]:
            if instruction.read_symbol == char_under_head:
                self.exec_instuction(instruction)
                return True
        return False

    def reset_machine(self):
        self.__head_index = 0
        self.__curent_state = 0

    def process(self, string_to_process=""):
        self.set_tape(string_to_process=string_to_process)
        while not self.is_final_state():
            track = self.step()
            if not track:
                self.reset_machine()
                return False
        self.reset_machine()
        return True
