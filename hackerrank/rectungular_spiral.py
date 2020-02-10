def rectangular_spiral(first_point, second_point):
    X, Y = 0, 1

    res = []

    if first_point[X] == second_point[X] and first_point[Y] == second_point[Y]:
        res.append(first_point)
        res.append(second_point)
        return res

    min_x, min_y, max_x, max_y = min(first_point[X], second_point[X]), \
                                 min(first_point[Y], second_point[Y]), \
                                 max(first_point[X], second_point[X]),\
                                 max(first_point[Y], second_point[Y])

    cur_corner = first_point[:]

    should_decrease_max_y = True
    if first_point[X] < second_point[X] and first_point[Y] > second_point[Y]:
        should_decrease_max_y = False

    should_decrease_max_x = True
    if first_point[X] > second_point[X] and first_point[Y] > second_point[Y]:
        should_decrease_max_x = False

    should_increase_min_x = True
    if first_point[X] < second_point[X] and first_point[Y] < second_point[Y]:
        should_increase_min_x = False

    should_increase_min_y = True
    if first_point[X] > second_point[X] and first_point[Y] < second_point[Y]:
        should_increase_min_y = False

    while True:
        res.append(cur_corner)

        if cur_corner[X] == min_x and cur_corner[X] == max_x and cur_corner[Y] == min_y and cur_corner[Y] == max_y:
            break

        if min_x == max_x and min_y == max_y:
            break
        elif cur_corner[X] == max_x and cur_corner[Y] == min_y and cur_corner[Y] != max_y:      # going DOWN
            cur_corner = [max_x, max_y]
            if should_increase_min_y:
                min_y += 1
            else:
                should_increase_min_y = True
            if min_x == max_x:
                min_y = max_y
        elif cur_corner[Y] == max_y and cur_corner[X] == max_x and cur_corner[X]!= min_x:    # going LEFT
            cur_corner = [min_x, max_y]
            if should_decrease_max_x:
                max_x -= 1
            else:
                should_decrease_max_x = True
            if min_y == max_y:
                min_x = max_x
        elif cur_corner[X] == min_x and cur_corner[Y] == max_y and cur_corner[Y] != min_y:    # going UP
            cur_corner = [min_x, min_y]
            if should_decrease_max_y:
                max_y -= 1
            else:
                should_decrease_max_y = True
            if min_x == max_x:
                min_y = max_y
        elif cur_corner[Y] == min_y and cur_corner[X] == min_x and cur_corner[X] != max_x:    # going RIGHT
            cur_corner = [max_x, min_y]
            if should_increase_min_x:
                min_x += 1
            else:
                should_increase_min_x = True
            if min_y == max_y:
                min_x = max_x
        else:
            break

    return res


first_point = [0, 0]
second_point = [4, 3]
r = rectangular_spiral(first_point, second_point)
print r
assert len([[0,0], [4,0], [4,3], [0,3], [0,1], [3,1], [3,2], [1,2]]) == len(r)
for e in [[0,0], [4,0], [4,3], [0,3],[0,1],
          [3,1], [3,2],
          [1,2]]:
    assert e in r

first_point = [5, 4]
second_point = [5, 4]
r = rectangular_spiral(first_point, second_point)
print r
for e in [[5, 4], [5, 4]]:
    assert e in r


first_point = [1, 3]
second_point = [3, 1]
res = [[1,3], [1,1], [3,1], [3,3], [2,3], [2,2]]
r = rectangular_spiral(first_point, second_point)
print r
assert len(r) == len(res)
for e in res:
    assert e in r


first_point = [7, 3]
second_point = [1, 2]
r = rectangular_spiral(first_point, second_point)
print r
for e in [[7,3], [1,3], [1,2], [7,2]]:
    assert e in r


first_point = [95, 2]
second_point = [2, 2]
r = rectangular_spiral(first_point, second_point)
assert len(r) == len([[95,2], [2,2]])
for e in [[95,2], [2,2]]:
    assert e in r

first_point = [2, 0]
second_point = [0, 5]
res = [[2,0], [2,5], [0,5], [0,0], [1,0], [1,4]]
r = rectangular_spiral(first_point, second_point)
print r
assert len(res) == len(r)
for e in res:
    assert e in r


first_point = [9, 1]
second_point = [0, 0]
res = [[9,1], [0,1], [0,0], [9,0]]
r = rectangular_spiral(first_point, second_point)
print r
assert len(res) == len(r)
for e in res:
    assert e in r


first_point = [7, 3]
second_point = [1, 2]
res = [[7,3], [1,3], [1,2], [7,2]]
r = rectangular_spiral(first_point, second_point)
assert len(res) == len(r)
for e in res:
    assert e in r

first_point = [0, 99]
second_point = [0, 0]
res = [[0,99], [0,0]]
r = rectangular_spiral(first_point, second_point)
assert len(res) == len(r)
for e in res:
    assert e in r