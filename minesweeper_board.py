import random

#
#   Given board size: width x height and number of bombs
#   return minesweeper's board filled with randomly distributed bombs
#   with neighbourhood cells containing numbers of bombs in adjustment cells
#


def show_board(a):

    for row in a:
        for cell in row:
            print cell,
        print ""


def create_board(width, height, num_bombs):

    if width <= 0 or height <= 0:
        print("Size of board should be bigger than 0")

    if num_bombs <= 0:
        print("Number of bombs should be bigger than 0")

    max_cell_idx = width * height

    if num_bombs > max_cell_idx:
        return [['X' for _ in xrange(width)] for _ in xrange(height)]

    bombs_idx = set()
    while len(bombs_idx) != num_bombs:
        bombs_idx.add(random.randint(0, max_cell_idx))

    neighbours = {}

    for idx in bombs_idx:
        y, x = idx / width, idx % width

        for y_idx in xrange(max(0, y-1), 1 + min(y+1, height-1)):
            for x_idx in xrange(max(0, x - 1), 1 + min(x + 1, width - 1)):
                if y_idx == y and x_idx == x:
                    continue
                neighbours[(y_idx, x_idx)] = neighbours.get((y_idx, x_idx), 0) + 1

    a = []

    for y in xrange(height):
        row = []
        for x in xrange(width):
            if y * width + x in bombs_idx:
                row.append('X')
            elif (y, x) in neighbours:
                row.append(neighbours[(y, x)])
            else:
                row.append(0)

        a.append(row)

    return a


w = create_board(10, 10, 30)

show_board(w)

