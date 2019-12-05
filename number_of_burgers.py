#
#   https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
#


def number_of_burgers(tomatoSlices, cheeseSlices):
    #
    #   tomatoSlices - 4*x - 2*y = 0
    #   cheeseSlices - x - y = 0
    #
    #   x = cheeseSlices - y
    #
    #   tomatoSlices - 4*cheeseSlices + 4*y - 2*y = 0
    #   tomatoSlices - 4*cheeseSlices + 2*y = 0
    #   2y = 4*cheeseSlices - tomatoSlices
    #
    #   y = (4*cheeseSlices - tomatoSlices) / 2
    #   X = cheeseSlices - Y
    #
    res = 4 * cheeseSlices - tomatoSlices
    if res % 2 or res < 0:
        return []

    total_small = res / 2
    total_jumbo = cheeseSlices - total_small

    if total_jumbo >= 0:
        return [total_jumbo, total_small]

    return []


def version_tle(tomatoSlices, cheeseSlices):
    total = cheeseSlices

    if not cheeseSlices:
        return [0, 0]

    for i in xrange(total):
        small = total - i
        if small*2 + 4*i-tomatoSlices == 0:
            return [i, small]

    return []


print number_of_burgers(tomatoSlices=16, cheeseSlices=7)
print version_tle(tomatoSlices=16, cheeseSlices=7)

print number_of_burgers(tomatoSlices=17, cheeseSlices=4)
print version_tle(tomatoSlices=17, cheeseSlices=4)

print number_of_burgers(tomatoSlices=2537427, cheeseSlices=860448)
print version_tle(tomatoSlices=2537427, cheeseSlices=860448)

print version_tle(tomatoSlices=0, cheeseSlices=0)

print version_tle(tomatoSlices=10, cheeseSlices=10)
