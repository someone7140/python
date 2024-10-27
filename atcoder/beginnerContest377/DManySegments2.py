import copy
import math
from typing import List

n, m = map(int, input().split())

zahyou_list = [0] * m

for i in range(n):
    l, r = map(int, input().split())
    l == l - 1
    r - r - 1
    if l == r:
        zahyou_list[l] = 2
    else:
        for j in range(l, r):
            zahyou_list[j] = 1
        zahyou_list[r] = 2

start = 0
end = 0
result = 0

while start == n or end == n:
    # 最初と最後が同一座標
    if start == end:
        if zahyou_list[end] == 2:
            result = result + math.factorial(end - start + 1)
            start = start + 1
            end = end + 1
        else:
            end = end + 1
    else:
        if zahyou_list[end] == 2:
            # 一つ前までで足す
            result = result + math.factorial(end - start)
            # 一つ前がつながっているか
            if zahyou_list[end - 1] == 1:
                start = start + 1
            end = end = end + 1
        else:
            end = end + 1

print(result)
