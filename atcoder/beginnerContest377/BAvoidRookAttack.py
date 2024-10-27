import copy
from typing import List


list_list_input: List[List[str]] = []

for i in range(8):
    s_list = list(input())
    list_list_input.append(s_list)

copy_list_list = copy.deepcopy(list_list_input)

for i in range(8):
    for j in range(8):
        cell = list_list_input[i][j]
        if cell == "#":
            # 上方向
            for ue_i in range(0, i):
                copy_list_list[ue_i][j] = "#"
            # 下方向
            for shita_i in range(i, 8):
                copy_list_list[shita_i][j] = "#"
            # 右方向
            for migi_J in range(j, 8):
                copy_list_list[i][migi_J] = "#"
            # 左方向
            for hidari_j in range(0, j):
                copy_list_list[i][hidari_j] = "#"

result = 0
for i in range(8):
    for j in range(8):
        if copy_list_list[i][j] == ".":
            result = result + 1

print(result)
