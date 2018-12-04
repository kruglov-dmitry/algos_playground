import itertools


# State 0: L = 0, R = 1
#
# Command "L": L = 2 * L - R
# Command "R": R = 2 * R - L
#
# Input:
# Output: shortest command sequence to get this number equal to L or R


def compute_number_according_to_sequence(sequence, L=0, R=1):
    for command in sequence:
        if command == "L":
            L = 2 * L - R
        elif command == "R":
            R = 2 * R - L

    return L, R


def generate_possible_commands(max_len, options):

    return map(list, [p for p in itertools.product(options, repeat=max_len)])


def find_command_sequence(target_num):

    init_cnt = 1

    while True:
        sequence_with_length = generate_possible_commands(init_cnt, ["L", "R"])

        for commands in sequence_with_length:
            L, R = compute_number_according_to_sequence(commands, 0, 1)

            if L == target_num or R == target_num:
                return commands
        init_cnt += 1


target_num = int(raw_input('Input target number '))

res = find_command_sequence(target_num)
print res
