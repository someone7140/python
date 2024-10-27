import copy
from typing import List

n, m = map(int, input().split())

result = n * n
initial_set = set()

for i in range(m):
    initial_set.add(input())

ng_set = copy.deepcopy(initial_set)

for zahyou in initial_set:
    i, j = map(int, zahyou.split())
    # 左上一個目
    if i > 1 and j > 2:
        new_i = i - 1
        new_j = j - 2
        ng_set.add(str(new_i) + " " + str(new_j))
    # 左上一個目
    if i > 2 and j > 1:
        new_i = i - 2
        new_j = j - 1
        ng_set.add(str(new_i) + " " + str(new_j))
    # 右上一個目
    if i > 2 and j < n:
        new_i = i - 2
        new_j = j + 1
        ng_set.add(str(new_i) + " " + str(new_j))
    # 右上二個目
    if i > 1 and j < n - 1:
        new_i = i - 1
        new_j = j + 2
        ng_set.add(str(new_i) + " " + str(new_j))
    # 右下一個目
    if i < n and j < n - 1:
        new_i = i + 1
        new_j = j + 2
        ng_set.add(str(new_i) + " " + str(new_j))
    # 右下二個目
    if i < n - 1 and j < n:
        new_i = i + 2
        new_j = j + 1
        ng_set.add(str(new_i) + " " + str(new_j))
    # 左下一個目
    if i < n - 1 and j > 1:
        new_i = i + 2
        new_j = j - 1
        ng_set.add(str(new_i) + " " + str(new_j))
    # 左下二個目
    if i < n and j > 2:
        new_i = i + 1
        new_j = j - 2
        ng_set.add(str(new_i) + " " + str(new_j))

print(result - len(ng_set))
