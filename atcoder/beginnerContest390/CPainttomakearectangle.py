from typing import List


h, w = map(int, input().split())

s_list_list: List[List[str]] = []
visit_list_list = [[0 for j in range(h)] for i in range(w)]

for i in range(h):
    s_list = list(input())
    s_list_list.append(s_list)

result = "Yes"
# 左上の座標
start_x: int | None = None
start_y: int | None = None
# 左下の座標
start_x1: int | None = None
start_y1: int | None = None

tansaku_flag = False


def proceed_func(now_x: int, now_y: int):
    global visit_list_list
    global s_list_list
    global h
    global w
    global result

    # 上に行く


for i2 in range(w):
    for i in range(h):
        masu = s_list_list[i][i2]
        if masu == "#":
            if tansaku_flag == False:
                visit_list_list[i][i2] = 1
                start_x = i2
                start_y = i
                if i2 == w - 1:
                    start_x1 = i2
                    start_y1 = i
            else:
                result = "No"
                break


if start_x == None:
    print("No")
else:
    print(result)
