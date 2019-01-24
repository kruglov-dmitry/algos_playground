# from profilehooks import timecall

import sys

#
#   Given 1 <= N <= 10000, numbers within range [1, 2**10000] verify that all of them have
#   single set bit in different positions
#   Constraints: 2.6 seconds, 9 MB

#
#               Initial version
#

def count_leading_zeros(x):
    """
    :param x: x < 2**10000,  yeap, this freakingly huge number
    :return: number of leading zeros from LEFT site of binary representation
    """
    n = 10000
    y = x >> 5000
    if y != 0:
        x = y
        n = n - 5000

    y = x >> 2500
    if y != 0:
        n = n - 2500
        x = y

    y = x >> 1250
    if y != 0:
        n = n - 1250
        x = y

    y = x >> 625
    if y != 0:
        n = n - 625
        x = y

    y = x >> 313
    if y != 0:
        n = n - 313
        x = y

    y = x >> 312
    if y != 0:
        n = n - 312
        x = y

    y = x >> 156
    if y != 0:
        n = n - 156
        x = y

    y = x >> 78
    if y != 0:
        n = n - 78
        x = y

    # 77
    y = x >> 39
    if y != 0:
        n = n - 39
        x = y

    y = x >> 20
    if y != 0:
        n = n - 20
        x = y

    y = x >> 19
    if y != 0:
        n = n - 19
        x = y

    y = x >> 10
    if y != 0:
        n = n - 10
        x = y

    y = x >> 9
    if y != 0:
        n = n - 9
        x = y

    y = x >> 5
    if y != 0:
        n = n - 5
        x = y

    y = x >> 4
    if y != 0:
        n = n - 4
        x = y

    y = x >> 2
    if y != 0:
        n = n - 2
        x = y

    y = x >> 1
    if y != 0:
        return n - 2
    return n - x

def count_trailing_zeros(x):
    """
    :param x: x < 2**10000, yeap, this freakingly huge number
    :return: number of trailing zeros from RIGHT site of binary representation
    """
    n = 0

    if x & 2**5000-1 == 0:
        n += 5000
        x >>= 5000

    if x & 2**2500-1 == 0:
        n += 2500
        x >>= 2500

    if x & 2**1250-1 == 0:
        n += 1250
        x >>= 1250

    if x & 2**625-1 == 0:
        n += 625
        x >>= 625

    if x & 2**312-1 == 0:
        n += 312
        x >>= 312

    # 313
    if x & 2**156-1 == 0:
        n += 156
        x >>= 156

    # 157
    if x & 2**80-1 == 0:
        n += 80
        x >>= 80

    # 77
    if x & 2**45-1 == 0:
        n += 45
        x >>= 45
    #
    if x & 0xFFFFFFFF == 0:
        n += 32
        x >>= 32
    if x & 0xFFFF == 0:
        n += 16
        x >>= 16
    if x & 0xFF == 0:
        n += 8
        x >>= 8
    if x & 0xF == 0:
        n += 4
        x >>= 4
    if x & 0x3 == 0:
        n += 2
        x >>= 2
    if x & 0x1 == 0:
        n += 1
    return n

def count_set_bit(n):
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1

    return cnt

@timecall
def test_case_1():
    matrix_size = 10000
    all_ored = 0

    for x in xrange(matrix_size):
        new_num = 2**x
        last_one = count_trailing_zeros(new_num)
        first_one = count_leading_zeros(new_num)
        idx = first_one + last_one + 1 == 10000
        if not idx:
            print "WaS here?", x, new_num, last_one, first_one
            break
        else:
            all_ored = all_ored | new_num   # ???

    wtf = count_set_bit(all_ored)
    print wtf
    if wtf == matrix_size:
        print(1)
    else:
        print(0)

#test_case_1()


if __name__ == '__main__':

    num_test_cases = int(sys.stdin.readline().strip())

    while num_test_cases:
        matrix_size = int(sys.stdin.readline().strip())

        all_ored = 0

        cnt = 0
        should_skip_to_next = False
        while cnt != matrix_size:
            cnt += 1
            new_num = int(sys.stdin.readline().strip())

            if should_skip_to_next:
                continue

            last_one = count_trailing_zeros(new_num)

            first_one = count_leading_zeros(new_num)

            # print first_one, last_one, "NUM:", new_num

            idx = first_one + last_one + 1 == 10000
            if not idx:
                should_skip_to_next = True
            else:
                all_ored = all_ored | new_num   # ???

        if not should_skip_to_next:
            wtf = count_set_bit(all_ored)
            if wtf == matrix_size:
                print(1)
            else:
                print(0)
        else:
            print(0)

        num_test_cases -= 1

#
#               Initial speed & memory optimized version
#

def ctz(x):
    n = 0
    for d in [5000, 2500, 1250, 625, 313, 156, 78, 39, 20, 10, 5, 3, 2, 1]:
        if x & (1<< d) - 1 == 0:
            n += d
            x >>= d
    return n


def clz(x):
    n = 10000
    for d in [5000, 2500, 1250, 625, 313, 156, 78, 39, 20, 10, 5, 3, 2, 1]:
        y = x >> d
        if y != 0:
            x = y
            n -= d

    return n - x


if __name__ == '__main__':

    tc = int(sys.stdin.readline().strip())

    while tc:
        sz = int(sys.stdin.readline().strip())
        skip = False
        rr = 0
        cnt = 0
        for buf in sys.stdin:
            if not skip:
                nn = int(buf)
                if nn != 0:
                    if ctz(nn) + clz(nn) == 9999:
                        rr = rr | nn
                    else:
                        skip = True

            cnt += 1
            if cnt == sz:
                break

        cnt = 0
        while rr:
            cnt += rr & 1
            rr >>= 1

        if cnt == sz:
            print(1)
        else:
            print(0)

        tc -= 1

#
#               Version with manual buffered reading from stdin
#               NOTE: no any memory advantage in comparisson to generators
#               approach
#

if __name__ == '__main__':

    num_test_cases = int(sys.stdin.readline().strip())

    sz = 0
    cnt = 0
    last_num = 0
    rr = 0
    error = False

    while num_test_cases:
        buf = sys.stdin.read(1000)
        ll = len(buf)
        if ll == 0:
            print(num_test_cases)
            raise
        start = end = 0
        while end != ll:
            if buf[end] != '\n':
                end += 1
            elif sz == 0:
                if end != start:
                    sz = last_num*10**(end-start) + int(buf[start:end])
                else:
                    sz = last_num
                last_num = 0
                end += 1
                start = end
            else:
                if not error:
                    if end != start:
                        num = last_num*10**(end-start) + int(buf[start:end])
                    else:
                        num = last_num

                    i0 = ctz(num)
                    i1 = clz(num)

                    if i1 + i0 + 1 != 10000:
                        error = True
                    else:
                        rr = rr | num   # ???

                last_num = 0
                end += 1
                start = end

                cnt += 1
                if sz == cnt:
                    if error:
                        print(0)
                    else:
                        if count_set_bit(rr) == sz:
                            print(1)
                        else:
                            print(0)

                    num_test_cases -= 1
                    rr = 0
                    error = False
                    cnt = 0
                    sz = 0


        if start != end:
            last_num = last_num*10**(end-start) + int(buf[start:end])

    print (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)



#
#           Final memory & speed optimized version
#

import sys

tc = int(sys.stdin.readline().strip())

while tc:
    sz = int(sys.stdin.readline().strip())
    rr = 1 << sz

    while sz:
        x1 = x2 = int(sys.stdin.readline().strip())
        if rr != -1:
            n1 = 0
            n2 = 10000
            for d in (5000, 2500, 1250, 625, 313, 156, 78, 39, 20, 10, 5, 3, 2, 1):
                if x1 & ((1 << d) - 1) == 0:
                    n1 += d
                    x1 >>= d
                y = x2 >> d
                if y:
                    x2 = y
                    n2 -= d
            n2 -= x2

            if n1 + n2 == 9999:
                rr |= (1 << n1)
            else:
                rr = -1
        sz -= 1

    print(int(rr != -1 and ((rr + 1) & rr) == 0))

    tc -= 1
