#
#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#


def best_time_to_buy_and_sell_stock(arr):

    if len(arr) < 2:
        return 0

    cur_min = min(arr[0], arr[1])
    best_profit = max(0, arr[1]-arr[0])
    for r in arr[2:]:
        cur_min = min(cur_min, r)
        cur_profit = max(best_profit, r-cur_min)
        if cur_profit > best_profit:
            best_profit = cur_profit

    return best_profit



arr = [7,1,5,3,6,4]
# 1-7 = -6
# 5-1=4, 5-7=-2
# 3-5=-2, 3-1=2, 3-7=-4

arr = [7,6,4,3,1]

print best_time_to_buy_and_sell_stock(arr)