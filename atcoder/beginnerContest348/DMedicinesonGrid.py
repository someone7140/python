from dataclasses import dataclass
import sys
from typing import Dict, List, Set, TypedDict


h, w = map(int, input().split())


@dataclass
class Masu:
    id: str
    syubetu: str
    ene: int


list_xy: List[List[Masu]] = []

start_x = -1
start_y = -1
end_x = -1
end_y = -1

for i in range(h):
    a_list = list(input())
    row: List[Masu] = []
    for j, a in enumerate(a_list):
        if a == "S":
            start_x = j
            start_y = i
        elif a == "T":
            end_x = j
            end_y = i
        row.append(Masu(str(j) + "-" + str(i), a, 0))

    list_xy.append(row)

n = int(input())
for i in range(n):
    r, c, e = map(int, input().split())
    y = r - 1
    x = c - 1
    list_xy[y][x] = Masu(list_xy[y][x].id, list_xy[y][x].syubetu, e)

result = "No"

saidai_ene_dict: Dict[str, int] = {}

sys.setrecursionlimit(200000000)


def proceed_func(
    now_x: int, now_y: int, now_masu: Masu, already_set: Set[str], ene: int
):
    global result
    global saidai_ene_dict
    global list_xy

    if result == "Yes":
        return

    # すでに訪れているか
    if now_masu.id in already_set:
        return

    # エネルギーの比較
    zan_ene = ene
    if zan_ene < now_masu.ene:
        zan_ene = now_masu.ene
    if zan_ene < 1:
        return
    saidai_ene = saidai_ene_dict.get(now_masu.id, -1)
    if saidai_ene > zan_ene:
        return

    saidai_ene_dict[now_masu.id] = zan_ene

    # 進む
    already_set.add(now_masu.id)

    # 上
    if now_y > 0:
        next_y = now_y - 1
        next_masu = list_xy[next_y][now_x]

        if next_masu.syubetu == "T":
            result = "Yes"
            return
        elif next_masu.syubetu != "#":
            next_ene = zan_ene - 1
            proceed_func(now_x, next_y, next_masu, already_set, next_ene)

    # 下
    if now_y < h - 1:
        next_y = now_y + 1
        next_masu = list_xy[next_y][now_x]

        if next_masu.syubetu == "T":
            result = "Yes"
            return
        elif next_masu.syubetu != "#":
            next_ene = zan_ene - 1
            proceed_func(now_x, next_y, next_masu, already_set, next_ene)

    # 左
    if now_x > 0:
        next_x = now_x - 1
        next_masu = list_xy[now_y][next_x]

        if next_masu.syubetu == "T":
            result = "Yes"
            return
        elif next_masu.syubetu != "#":
            next_ene = zan_ene - 1
            proceed_func(next_x, now_y, next_masu, already_set, next_ene)

    # 右
    if now_x < w - 1:
        next_x = now_x + 1
        next_masu = list_xy[now_y][next_x]

        if next_masu.syubetu == "T":
            result = "Yes"
            return
        elif next_masu.syubetu != "#":
            next_ene = zan_ene - 1
            proceed_func(next_x, now_y, next_masu, already_set, next_ene)

    # 自分の座標をSetから削除
    already_set.remove(now_masu.id)


proceed_func(start_x, start_y, list_xy[start_y][start_x], set(), 0)

print(result)
