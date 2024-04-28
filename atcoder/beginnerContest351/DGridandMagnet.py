import copy
import sys
from typing import List, Set

sys.setrecursionlimit(200000000)
h, w = map(int, input().split())
hw_list: List[List[str]] = []
score_list_list = [[0] * w for _ in range(h)]
already_list_list_empty = [[0] * w for _ in range(h)]
max_result = 1

for i in range(h):
    w_list = list(input())
    hw_list.append(w_list)


def check_tonari_jisyaku(input_h, input_w):
    global hw_list

    if input_h > 0:
        if hw_list[input_h - 1][input_w] == "#":
            return True
    if input_h < h - 1:
        if hw_list[input_h + 1][input_w] == "#":
            return True

    if input_w > 0:
        if hw_list[input_h][input_w - 1] == "#":
            return True
    if input_w < w - 1:
        if hw_list[input_h][input_w + 1] == "#":
            return True

    return False


def saiki_masu(
    input_h: int,
    input_w: int,
    masu_list_list: List[List[int]],
    already_list_list: List[List[int]],
):

    if already_list_list[input_h][input_w] == 1:
        return

    already_list_list[input_h][input_w] = 1
    masu_list_list.append([input_h, input_w])
    if check_tonari_jisyaku(input_h, input_w):
        return

    if input_h > 0:
        if hw_list[input_h - 1][input_w] != "#":
            saiki_masu(input_h - 1, input_w, masu_list_list, already_list_list)
    if input_h < h - 1:
        if hw_list[input_h + 1][input_w] != "#":
            saiki_masu(input_h + 1, input_w, masu_list_list, already_list_list)
    if input_w > 0:
        if hw_list[input_h][input_w - 1] != "#":
            saiki_masu(input_h, input_w - 1, masu_list_list, already_list_list)
    if input_w < w - 1:
        if hw_list[input_h][input_w + 1] != "#":
            saiki_masu(input_h, input_w + 1, masu_list_list, already_list_list)


for i in range(h):
    for j in range(w):
        masu = hw_list[i][j]
        if masu == ".":
            if check_tonari_jisyaku(i, j):
                score_list_list[i][j] = 1
            else:
                if score_list_list[i][j] < 1:
                    masu_list_list: List[List[int]] = []
                    already_list = copy.deepcopy(already_list_list_empty)

                    saiki_masu(i, j, masu_list_list, already_list)
                    len_temp = len(masu_list_list)

                    if len_temp > max_result:
                        max_result = len_temp
                    for masu_index in masu_list_list:
                        if score_list_list[masu_index[0]][masu_index[1]] < 1:
                            score_list_list[masu_index[0]][masu_index[1]] = len_temp

print(max_result)
