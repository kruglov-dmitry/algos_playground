import argparse
import os
import sys

#
#   Requires python 3.6+ because of string interpolation:
#   https://www.programiz.com/python-programming/string-interpolation
#


VALUES = 'values'
DIFFS = 'differences'
METRIC_OPTS = [VALUES, DIFFS]

DEBUG = False


def consecutive_sum(numbers, max_length=None, metric=VALUES):

    if metric != VALUES:
        numbers = [abs(j-i) for i, j in zip(numbers, numbers[1:])]
        if max_length:
            max_length -= 1

    ll = len(numbers)

    max_sum = -sys.maxsize
    idxes = None

    if ll == 0:
        return max_sum, idxes

    if not max_length:
        max_length = ll

    cache = {}

    for x in range(ll):
        cache[x] = {}
        cache[x][x] = numbers[x]
        if cache[x][x] > max_sum:
            max_sum = cache[x][x]
            idxes = (x, x)
        end_idx = min(ll, x+max_length)
        for y in range(x+1, end_idx):

            cache[x][y] = cache[x][y-1] + numbers[y]
            if cache[x][y] > max_sum:
                max_sum = cache[x][y]
                idxes = (x, y)

    if DEBUG:
        print(idxes)

    return max_sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Given a list of integers, find the consecutive, non-empty subsequence '
                    'with the highest sum according to metric.')
    parser.add_argument('file_name', metavar='file_name', type=str,
                        help='file name containing array of numbers for analysis')
    parser.add_argument('n', metavar='number_of_elements', type=int, nargs='?', default=None,
                        help='restricts the maximum length of the subsequence to n')
    parser.add_argument('metric', metavar='metric', type=str, nargs='?', choices=METRIC_OPTS,
                        default=VALUES,
                        help='Provide desired metric for computations. Options are: values, differences')

    args = parser.parse_args()

    if not os.path.isfile(args.file_name):
        print(f"File {args.file_name} is not found")
        sys.exit(1)

    numbers = None
    with open(args.file_name, 'r') as src:
        try:
            numbers = list(map(int, src.readline().split()))
        except Exception as e:
            print(f"Can't parse file content: {e}!")
            sys.exit(1)

    print(consecutive_sum(numbers, args.n, args.metric))