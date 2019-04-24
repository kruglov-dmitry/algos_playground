#
#   https://leetcode.com/problems/excel-sheet-column-number/
#
#   Given excell sheet name - return corresponding column number
#


def excel_sheet_column_number(s):
    step = 25
    initial = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
               "F":6, "G": 7, "H": 8, "I": 9, "J": 10,
               "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
               "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
               "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
               }
    l = len(s)
    if l == 0:
        return 0

    idx = 0
    res = initial[s[idx]]

    while idx < l-1:
        idx += 1
        res += res * step + initial[s[idx]]

    return res

# ZY = 701
# AAA = 703