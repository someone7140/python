from dataclasses import dataclass
import math
import sys
from typing import List
import itertools

n, s, t = map(int, input().split())
result = sys.maxsize


@dataclass
class Zahyou:
    ab: List[int]
    cd: List[int]


zahyou_list: List[Zahyou] = []
index_list: List[int] = []
syousya_total = 0

for i in range(n):
    a, b, c, d = map(int, input().split())
    syousya_total = syousya_total + math.sqrt((a - c) * (a - c) + (b - d) * (b - d)) / t
    zahyou_list.append(Zahyou([a, b], [c, d]))
    index_list.append(i)

idou_total = sys.maxsize
junretsu = list(itertools.permutations(index_list, n))


def saiki_idou(
    index: int,
    index_temp_list: List[int],
    now_x: int,
    now_y: int,
    idou_total_param: int,
):
    global n
    global idou_total
    global junretsu

    if index == n:
        if idou_total_param < idou_total:
            idou_total = idou_total_param
    else:
        temp_i = index_temp_list[index]
        ab = zahyou_list[temp_i].ab
        cd = zahyou_list[temp_i].cd

        # 1パターン目
        idou_temp = (
            math.sqrt(
                (ab[0] - now_x) * (ab[0] - now_x) + (ab[1] - now_y) * (ab[1] - now_y)
            )
            / s
        )
        temp_idou_total = idou_total_param + idou_temp
        saiki_idou(index + 1, index_temp_list, cd[0], cd[1], temp_idou_total)

        # 2パターン目
        idou_temp = (
            math.sqrt(
                (cd[0] - now_x) * (cd[0] - now_x) + (cd[1] - now_y) * (cd[1] - now_y)
            )
            / s
        )
        temp_idou_total = idou_total_param + idou_temp
        saiki_idou(index + 1, index_temp_list, ab[0], ab[1], temp_idou_total)


for index_list_temp in junretsu:
    saiki_idou(0, index_list_temp, 0, 0, 0)


print(syousya_total + idou_total)
