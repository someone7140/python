from typing import List


n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list_sorted = sorted(a_list, reverse=True)
b_list_sorted = sorted(b_list, reverse=True)

zan_list: List[int] = []

b_index = 0

for a in a_list_sorted:
    if b_index <= n - 2 and b_list_sorted[b_index] >= a:
        b_index = b_index + 1
    else:
        zan_list.append(a)


if len(zan_list) == 1:
    print(zan_list[0])
else:
    print(-1)
