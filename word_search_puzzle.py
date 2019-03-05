from collections import defaultdict

"""

We are given 8 cylinders with 10 edges with letter on every edge - wheels.
Each wheel can be moved into any position on the puzzle.
Not only does each wheel spin, but the order of the wheels can be changed.

Find wheel combinations that allow to reconstruct the word.

"""

cy1 = ["x", "u", "s", "a", "n", "e", "i", "w", "y", "o"]  # 0
cy2 = ["h", "e", "b", "i", "d", "u", "t", "a", "c", "o"]  # 1
cy3 = ["l", "i", "n", "a", "z", "u", "f", "o", "m", "e"]  # 2
cy4 = ["s", "u", "h", "o", "d", "e", "p", "a", "r", "i"]  # 3
cy5 = ["f", "a", "k", "n", "e", "r", "i", "l", "o", "b"]  # 4
cy6 = ["e", "j", "v", "a", "w", "d", "i", "q", "t", "r"]  # 5
cy7 = ["s", "g", "p", "e", "w", "t", "n", "v", "a", "l"]  # 6
cy8 = ["y", "o", "r", "c", "u", "g", "m", "t", "n", "e"]  # 7

wheels = [cy1, cy2, cy3, cy4, cy5, cy6, cy7, cy8]

WORD_LENGTH = 8
LAST_LETTER_IDX = WORD_LENGTH - 1


def find_combinations(word, wheels_by_letter, result):
    word_by_wheel = []

    ll = len(word)

    for idx in xrange(ll):
        letter = word[idx]
        if letter not in wheels_by_letter:
            return False

        cur_wheels = wheels_by_letter[letter]
        word_by_wheel.append(cur_wheels)

    letter_id = 0
    stack = [(letter_id, word_by_wheel[letter_id], [])]

    while stack:
        letter_id, wheel_ids_for_this_letter, exclude_list = stack.pop()
        for idx in wheel_ids_for_this_letter:
            if idx not in exclude_list and letter_id < LAST_LETTER_IDX:
                new_exclude_list = []
                for x in exclude_list:
                    new_exclude_list.append(x)
                new_exclude_list.append(idx)
                stack.append((letter_id + 1, word_by_wheel[letter_id + 1], new_exclude_list))
            elif idx not in exclude_list:
                for r in exclude_list:
                    result.append(r)
                result.append(idx)
                return True

    return False


def find_words(file_name):
    res = []

    wheels_by_letter = defaultdict(list)

    for idx, cy in enumerate(wheels):
        for l in cy:
            wheels_by_letter[l].append(idx)

    with open(file_name, 'r') as in_file:
        for word in in_file:
            wheels_combinations = []
            w = word.strip().lower()
            if find_combinations(w, wheels_by_letter, wheels_combinations):
                res.append((w, wheels_combinations))

    return res
