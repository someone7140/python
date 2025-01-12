import copy
from typing import List


n = int(input())
a_list = list(map(int, input().split()))
a_list_temp = copy.deepcopy(a_list)

result_list: List[str] = []
all_plus = 0

for i in range(n):
    temochi = a_list_temp[i] + all_plus
    # 自分が払うべき数
    haraubeki = n - i - 1
    if temochi >= haraubeki:
        all_plus = all_plus + 1
        result_list.append(str(temochi - haraubeki))
    else:
        for j in range(i + 1, i + temochi + 1):
            a_list_temp[j] = a_list_temp[j] + 1
        result_list.append(str(0))

print(" ".join(result_list))
