import itertools

#
#   Given array of numbers, sequence of mathematical operators and a target number.
#   Find an equation where every number will be used exactly once that will be resulted in target number.
#   Return None if it is not possible.
#
#   NOTE 1: NOT necessary to use all operators
#   NOTE 2: bonus point for implementation without usage of mathematical operators ar all
#

array = [2, 16, 1, 4, 64]
operators = ['*', '/', '-', '+']
# -2+4*64-16+1


def add(a, b):
    return a + b


def add_shift(a, b):
    while b:
        carry = a & b

        a = a ^ b

        b = carry << 1

    return a


def subtract(a, b):
    return a - b


def subtract_shift(a, b):
    while b:
        borrow = (~a) & b

        a = a ^ b

        b = borrow << 1

    return a


def multiply(a, b):
    return a * b


def multiply_shift(a, b):
    res = 0

    while b:
        if b & 1:
            res = add_shift(res, a)

        a = a << 1      # Double
        b = b >> 1      # Halve

    return res


def divide(a, b):
    return a / b


def divide_shift(a, b):
    if not b:
        raise ZeroDivisionError

    sign = -1 if ((a < 0) ^ (b < 0)) else 1

    dividend = abs(a)
    divisor = abs(b)

    quotient = 0
    while dividend >= divisor:
        dividend = subtract_shift(dividend, divisor)
        quotient = add_shift(quotient, 1)

    return sign * quotient


ops = {'*': multiply, '/': divide, '+': add, '-': subtract}
ops_shift = {'*': multiply_shift, '/': divide_shift, '+': add_shift, '-': subtract_shift}


def choose_op(op_symbol, use_bit_shifts=False):
    if use_bit_shifts:
        return ops_shift.get(op_symbol)

    return ops.get(op_symbol)


def compute_equation(sequence_ops, array, use_bit_shifts):
    res = array[0]
    for idx in xrange(4):
        method = choose_op(sequence_ops[idx], use_bit_shifts)
        res = method(res, array[idx + 1])

    return res


def solution(target_num, use_bit_shifts):
    for sequence_ops in map(list, itertools.product(operators, repeat=4)):
        for cur_array in itertools.permutations(array):
            if compute_equation(sequence_ops, cur_array, use_bit_shifts) == target_num:
                return sequence_ops, cur_array

    return None


print(solution(113, use_bit_shifts=False))
