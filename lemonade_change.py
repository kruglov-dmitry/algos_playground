#
#   https://leetcode.com/problems/lemonade-change/
#


def lemonade_change(bills):
    five_cnt, ten_cnt, twenty_cnt = 0, 0, 0

    for entry in bills:
        if entry == 5:
            five_cnt += 1
        elif entry == 10:
            if five_cnt:
                five_cnt -= 1
            else:
                return False
            ten_cnt += 1
        elif entry == 20:
            was_ten = False
            if ten_cnt:
                ten_cnt -= 1
                was_ten = True

            if five_cnt:
                five_cnt -= 1
                if not was_ten:
                    if five_cnt < 2:
                        return False
                    five_cnt -= 2
            else:
                return False

            twenty_cnt += 1

    return True
