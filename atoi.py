INT_MIN = -pow(2, 31)
INT_MAX = pow(2, 31) - 1

signs = {'-', '+'}
valid_symbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


class Solution(object):
    def myAtoi(self, some_str):
        """
        :type str: str
        :rtype: int
        """

        pure_str = some_str.strip()

        ll = len(pure_str)

        if ll < 1:
            return 0

        negative = False
        idx = 0
        if pure_str[idx] in signs:
            if pure_str[idx] == '-':
                negative = True
            idx += 1

        my_int = 0
        while idx < ll and pure_str[idx] in valid_symbols:
            my_int = my_int * 10 + int(pure_str[idx])
            idx += 1

        if negative:
            my_int = - my_int

        if my_int < INT_MIN:
            return INT_MIN

        if my_int > INT_MAX:
            return INT_MAX

        return my_int