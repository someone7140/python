from typing import Dict, List, Set


h, w, d = map(int, input().split())

s_list_list: List[List[str]] = []
s_dict: Dict[str, Set[List[int]]] = {}

for i in range(h):
    s_list = list(input())
    s_list_list.append(s_list)

s_key_list_list: List[List[str]] = []
for i in range(h):
    s_key_list = []
    for k in range(w):
        s_key_list.append(str(i) + "-" + str(k))
    s_key_list_list.append(s_key_list)


def saiki(now_h: int, now_w: int, now_d: int, zahyou_set: Set[str]):
    global d
    global s_list_list
    global s_key_list_list

    if now_d == 0:
        return zahyou_set
    else:
        if now_h > 0:
            temp_h = now_h - 1
            if s_list_list[temp_h][now_w] == ".":
                zahyou_set.add(s_key_list_list[temp_h][now_w])
            zahyou_set = zahyou_set | saiki(temp_h, now_w, now_d - 1, set())
        if now_h < h - 1:
            temp_h = now_h + 1
            if s_list_list[temp_h][now_w] == ".":
                zahyou_set.add(s_key_list_list[temp_h][now_w])
            zahyou_set = zahyou_set | saiki(temp_h, now_w, now_d - 1, set())
        if now_w > 0:
            temp_w = now_w - 1
            if s_list_list[now_h][temp_w] == ".":
                zahyou_set.add(s_key_list_list[now_h][temp_w])
            zahyou_set = zahyou_set | saiki(now_h, temp_w, now_d - 1, set())
        if now_w < w - 1:
            temp_w = now_w + 1
            if s_list_list[now_h][temp_w] == ".":
                zahyou_set.add(s_key_list_list[now_h][temp_w])
            zahyou_set = zahyou_set | saiki(now_h, temp_w, now_d - 1, set())

    return zahyou_set


for i in range(h):
    for k in range(w):
        if s_list_list[i][k] == ".":
            zahyou_set = saiki(i, k, d, {s_key_list_list[i][k]})
            s_dict[s_key_list_list[i][k]] = zahyou_set

s_dict_keys = list(s_dict)
s_dict_keys_len = len(s_dict_keys)
result = 0
for i in range(s_dict_keys_len):
    set1 = s_dict[s_dict_keys[i]]
    for i2 in range(i + 1, s_dict_keys_len):
        set2 = s_dict[s_dict_keys[i2]]
        temp_result = len(set1 | set2)
        if result < temp_result:
            result = temp_result

print(result)
