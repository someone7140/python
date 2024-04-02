from typing import List


n, k = map(int, input().split())

a_list = list(map(int, input().split()))

list_result: List[int] = []

for a in a_list:
    if a % k == 0:
        list_result.append(str(a // k))


print(" ".join(list_result))
