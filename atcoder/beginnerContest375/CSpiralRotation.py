import copy
from typing import List


n = int(input())

list_list_input: List[List[str]] = []
list_list_result: List[List[str]] = []
list_result: List[str] = []

for i in range(n):
    b_list = list(input())
    list_list_input.append(b_list)
    list_list_result.append(copy.deepcopy(b_list))

loop = n // 2
for i in range(n // 2):
    for j in range(i, n - i):
        # 上の行を右端にする
        list_list_result[j][n - 1 - i] = list_list_input[i][j]
        # 右の列を下にする
        list_list_result[n - 1 - i][j] = list_list_input[j][n - 1 - i]
        # 下の行を左端にする
        list_list_result[j][i] = list_list_input[n - 1 - i][j]
        # 左の列を上にする
        list_list_result[i][j] = list_list_input[j][i]

for row in list_list_result:
    list_result.append("".join(row))

print("\n".join(list_result))
