from typing import List, Set


h, w, x, y = map(int, input().split())

s_list_list: List[List[str]] = []

for i in range(h):
    s_list = list(input())
    s_list_list.append(s_list)

t_list = list(input())
home_set: Set[str] = set()

now_x = x - 1
now_y = y - 1

for command in t_list:
    if command == "U":
        if now_x > 0 and s_list_list[now_x - 1][now_y] != "#":
            now_x = now_x - 1
    if command == "D":
        if now_x < h - 1 and s_list_list[now_x + 1][now_y] != "#":
            now_x = now_x + 1
    if command == "L":
        if now_y > 0 and s_list_list[now_x][now_y - 1] != "#":
            now_y = now_y - 1
    if command == "R":
        if now_y < w - 1 and s_list_list[now_x][now_y + 1] != "#":
            now_y = now_y + 1

    if s_list_list[now_x][now_y] == "@":
        home_set.add(str(now_x) + "-" + str(now_y))

print(str(now_x + 1) + " " + str(now_y + 1) + " " + str(len(home_set)))
