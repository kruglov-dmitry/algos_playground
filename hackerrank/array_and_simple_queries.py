from profilehooks import timecall
import sys
from ImplicitTreap import ImplicitTreap

N, M = [int(i) for i in sys.stdin.readline().split()]

A = [int(i) for i in sys.stdin.readline().split()]

assert (len(A) == N)

Q = []
for line in sys.stdin:
    commands = [int(i) for i in line.split()]
    Q.append(commands)

assert (len(Q) == M)

@timecall
def brute_force(A, Q):
    while Q:
        cmd_type, start_idx, end_idx = Q.pop(0)
        tmp_arr = A[start_idx - 1:end_idx]
        if cmd_type == 1:
            A = tmp_arr + A[0:start_idx-1] + A[end_idx:]
        elif cmd_type == 2:
            A = A[0:start_idx-1] + A[end_idx:] + tmp_arr
        else:
            raise

        assert(len(A) == N)

    print(abs(A[0] - A[N - 1]))
    print(" ".join(str(x) for x in A))


@timecall
def treap_solution(A, Q):

    implicit_treap = ImplicitTreap()

    for entry in A:
        implicit_treap.insert(entry)

    cnt = 0
    while Q:
        cmd_type, start_idx, end_idx = Q.pop(0)

        if cmd_type == 1:
            implicit_treap.exec_command_1(start_idx, end_idx)
        elif cmd_type == 2:
            implicit_treap.exec_command_2(start_idx, end_idx)
        else:
            raise

        cnt += 1

    print(abs(implicit_treap.get_min() - implicit_treap.get_max()))
    implicit_treap.show()


# brute_force(A, Q)

treap_solution(A, Q)