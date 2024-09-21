from bisect import bisect_left
from typing import List

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_list_sorted = sorted(a_list)

minUpper = m // n

# 累積和
a_sum_list: List[int] = []
for i in range(n):
    if i == 0:
        a_sum_list.append(a_list_sorted[i])
    else:
        a_sum_list.append(a_sum_list[i - 1] + a_list_sorted[i])

if a_sum_list[n - 1] <= m:
    print("infinite")
    exit()

# 二分探索
left = 0
right = 1000000000000
half = 9999999999999

while right - left > 1:
    half = (left + right) // 2
    upper_index = bisect_left(a_list_sorted, half)
    if upper_index == 0:
        half = half + 1
        break
    total = a_sum_list[upper_index - 1] + half * (n - upper_index)
    if total > m:
        right = half
    else:
        total_r = a_sum_list[upper_index - 1] + right * (n - upper_index)
        if total_r <= m:
            half = right
            break
        else:
            left = half

print(half)
