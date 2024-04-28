import sys
from typing import List, Set


n = int(input())
a_list = list(map(int, input().split()))
a_result: List[int] = []
len_a = 0

sys.setrecursionlimit(200000000)


def saiki_exclude():
    global len_a
    global a_result

    if len_a < 2:
        return
    if a_result[len_a - 1] != a_result[len_a - 2]:
        return

    a_result.pop()
    len_a = len_a - 1
    a_result[len_a - 1] = a_result[len_a - 1] + 1
    saiki_exclude()


for a in a_list:
    if len_a < 1:
        a_result.append(a)
        len_a += 1
    else:
        if a_result[len_a - 1] != a:
            a_result.append(a)
            len_a += 1
        else:
            new_a = a + 1
            a_result[len_a - 1] = new_a
            saiki_exclude()

print(len(a_result))
