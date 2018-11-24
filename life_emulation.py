import random
import time

PROBABILITY = 0.7


class STATE:
    LIVE = 1
    DEAD = 0

#
#               Some test input
#

fff = \
    """
       X 
       XX
       X 
    
    
    """

glider = """


   X   
    X  
 XXXX  


"""


#
#               Whatever
#


def generate_test_input(width, height, probability=PROBABILITY):
    input = []
    for x in xrange(width):
        row = []
        for y in xrange(height):
            if random.random() < probability:
                state = STATE.DEAD
            else:
                state = STATE.LIVE

            row.append(state)

        input.append(row)

    return input


def read_input_from_string(multi_line_input):
    res = []

    rows = [s for s in multi_line_input.splitlines()]

    rows = rows[1:]

    for idy, row in enumerate(rows):

        this_row = []

        for idx, symbol in enumerate(row):
            if symbol == 'X':
                this_row.append(STATE.LIVE)
            else:
                this_row.append(STATE.DEAD)

        res.append(this_row)

    return res


#
#               Visualization
#


def show(input_state):
    res = ""
    for row in input_state:
        row_repr = ""
        for cell in row:
            if cell == STATE.DEAD:
                row_repr += ' '
            else:
                row_repr += 'X'
        res += row_repr + "\n"

    print res


def show_simple(input_state):
    for row in input_state:
        print str(row) + "\n"


def print_both_together(prev, current):

    str_repr = ""

    max_y = len(prev)
    max_x = len(prev[0])

    for y in xrange(max_y):
        row_repr = ""
        for x in xrange(max_x):
            if prev[y][x] == STATE.LIVE:
                row_repr += "X"
            else:
                row_repr += " "

        row_repr += "\t"

        for x in xrange(max_x):
            if current[y][x] == STATE.LIVE:
                row_repr += "X"
            else:
                row_repr += " "

        str_repr += row_repr + "\n"

    print str_repr


def get_num_of_live_neighbors_simple(x, y, input_state, max_x, max_y):
    res = 0

    # check for corners

    if x == 0 and y == 0:

        if max_y > 0 and input_state[1][x] == STATE.LIVE:
            res += 1
        if max_x > 0 and input_state[y][1] == STATE.LIVE:
            res += 1
        if max_y > 0 and max_x > 0 and input_state[1][1] == STATE.LIVE:
            res += 1

    elif x == max_x and y == max_y:

        if max_x > 0 and max_y > 0 and input_state[y - 1][x - 1] == STATE.LIVE:
            res += 1
        if max_y > 0 and input_state[y - 1][x] == STATE.LIVE:
            res += 1
        if max_x > 0 and input_state[y][x - 1] == STATE.LIVE:
            res += 1

    elif x == 0 and y == max_y:

        if max_y > 0 and input_state[y - 1][x] == STATE.LIVE:
            res += 1
        if max_y > 0 and max_x > 0 and input_state[y - 1][1] == STATE.LIVE:
            res += 1
        if max_x > 0 and input_state[y][1] == STATE.LIVE:
            res += 1

    elif x == max_x and y == 0:

        if max_x > 0 and input_state[y][x - 1] == STATE.LIVE:
            res += 1
        if max_y > 0 and max_x > 0 and input_state[y + 1][x - 1] == STATE.LIVE:
            res += 1
        if max_y > 0 and input_state[y + 1][x] == STATE.LIVE:
            res += 1

    # Edge lines

    elif x == 0 and 0 < y < max_y:

        for y_idx in [y - 1, y + 1]:
            if input_state[y_idx][x] == STATE.LIVE:
                res += 1

        for y_idx in xrange(y - 1, y + 2):
            if max_x > 0 and input_state[y_idx][x + 1] == STATE.LIVE:
                res += 1

    elif x == max_x and 0 < y < max_y:

        for y_idx in [y - 1, y + 1]:
            if input_state[y_idx][x] == STATE.LIVE:
                res += 1

        for y_idx in xrange(y - 1, y + 2):
            if input_state[y_idx][x - 1] == STATE.LIVE:
                res += 1

    elif y == 0 and 0 < x < max_x:

        for x_idx in [x - 1, x + 1]:
            if input_state[y][x_idx] == STATE.LIVE:
                    res += 1

        if max_y > 0:
            for x_idx in xrange(x - 1, x + 2):
                if input_state[y + 1][x_idx] == STATE.LIVE:
                    res += 1

    elif y == max_y and 0 < x < max_x:

        for x_idx in [x - 1, x + 1]:
            if input_state[y][x_idx] == STATE.LIVE:
                res += 1

        for x_idx in xrange(x - 1, x + 2):
            if input_state[y - 1][x_idx] == STATE.LIVE:
                res += 1

    # Finally - all others

    else:

        # NOTE: xrange is exclusive
        for x_idx in xrange(x - 1, x + 2):
            for y_idx in xrange(y - 1, y + 2):
                if x_idx == x and y_idx == y:
                    continue
                if input_state[y_idx][x_idx] == STATE.LIVE:
                    res += 1

    return res


def next_epoch(input_state, max_x, max_y):
    new_generation = []

    for y_idx, row in enumerate(input_state):

        new_row = []

        for x_idx, cell in enumerate(row):

            num_of_live_neighbors = get_num_of_live_neighbors_simple(x_idx, y_idx, input_state, max_x, max_y)

            new_state = cell

            if cell == STATE.LIVE:
                if num_of_live_neighbors < 2:
                    new_state = STATE.DEAD
                elif num_of_live_neighbors > 3:
                    new_state = STATE.DEAD
            elif cell == STATE.DEAD:
                if num_of_live_neighbors == 3:
                    new_state = STATE.LIVE

            new_row.append(new_state)

        new_generation.append(new_row)

    return new_generation


def should_stop(test_input, prev):

    # 1st condition - all are dead 0_0

    all_dead = True

    for row in test_input:
        for cell in row:
            if cell == STATE.LIVE:
                all_dead = False

    if all_dead:
        return all_dead

    # 2nd condition - check whether nothing is changed from last time
    for y, row in enumerate(test_input):
        for x, cell in enumerate(row):
            if test_input[y][x] != prev[y][x]:
                return False

    # 3rd condition to compare with previous states in history
    # TODO

    return True


def run_emulation(test_input):
    import copy

    prev = copy.deepcopy(test_input)

    max_y = len(test_input) - 1
    max_x = len(test_input[0]) - 1

    while True:
        show(test_input)
        time.sleep(1)
        test_input = next_epoch(test_input, max_x, max_y)
        if should_stop(test_input, prev):
            break


if __name__ == "__main__":
    test_input = read_input_from_string(glider)
    run_emulation(test_input)
