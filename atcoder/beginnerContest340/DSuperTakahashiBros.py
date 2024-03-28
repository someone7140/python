from dataclasses import dataclass
from sys import stdin
import sys
from typing import List


n = int(input())

abx = [list(map(int, stdin.readline().split())) for _ in range(n - 1)]

cost_array = [-1] * n
cost_array[0] = 0

sys.setrecursionlimit(200000000)


def saiki_stage(index: int, cost):
    global n
    global abx
    global cost_array

    # 転送ルート
    new_index = abx[index][2] - 1
    new_cost = cost + abx[index][1]
    if cost_array[new_index] == -1 or new_cost <= cost_array[new_index]:
        cost_array[new_index] = new_cost
        if new_index < n - 1:
            saiki_stage(new_index, new_cost)

    # そのまま下に進む
    new_index = index + 1
    new_cost = cost + abx[index][0]
    if cost_array[new_index] == -1 or new_cost <= cost_array[new_index]:
        cost_array[new_index] = new_cost
        if new_index < n - 1:
            saiki_stage(new_index, new_cost)


saiki_stage(0, 0)
print(cost_array[n - 1])
