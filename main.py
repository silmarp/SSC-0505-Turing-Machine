from models.turingMachine import TuringMachine


def main():
    number_states = int(input())
    alphabet = input()
    auxiliary_alphabet = input()
    final_state = int(input())
    n_of_instructions = int(input())
    instructions = []
    for i in range(n_of_instructions):
        instruction = input()
        instructions.append(instruction)

    machine = TuringMachine(number_states,
                            initial_state=0,
                            alphabet=alphabet[2:].split(),
                            extended_alphabet=auxiliary_alphabet[2:].split(),
                            final_state=final_state,
                            instructions=instructions,)

    n_of_strings = int(input())
    for i in range(n_of_strings):
        string = input()
        result = machine.process(string_to_process=string)
        if result:
            print("aceita")
        else:
            print("regeita")


if __name__ == "__main__":
    main()
