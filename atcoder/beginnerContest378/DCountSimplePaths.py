from typing import List


h, w, k = map(int, input().split())

hw_list_list: List[List[str]] = []
for i in range(h):
    w_list = list(input())
    hw_list_list.append(w_list)

visited_list_list = [[0] * w for _ in range(h)]
result = 0


def keiro(h_param, w_param, count):
    global k
    global h
    global w
    global visited_list_list
    global hw_list_list
    global result

    if visited_list_list[h_param][w_param] == 0:
        if count == k:
            result = result + 1
        else:
            visited_list_list[h_param][w_param] = 1
            # 上方向
            if h_param > 0 and hw_list_list[h_param - 1][w_param] == ".":
                keiro(h_param - 1, w_param, count + 1)
            # 下方向
            if h_param < h - 1 and hw_list_list[h_param + 1][w_param] == ".":
                keiro(h_param + 1, w_param, count + 1)
            # 左方向
            if w_param > 0 and hw_list_list[h_param][w_param - 1] == ".":
                keiro(h_param, w_param - 1, count + 1)
            # 右方向
            if w_param < w - 1 and hw_list_list[h_param][w_param + 1] == ".":
                keiro(h_param, w_param + 1, count + 1)

            visited_list_list[h_param][w_param] = 0


for h_i in range(h):
    for w_i in range(w):
        if hw_list_list[h_i][w_i] == ".":
            keiro(h_i, w_i, 0)

print(result)
