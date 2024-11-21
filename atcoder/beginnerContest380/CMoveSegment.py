from typing import List

n, k = map(int, input().split())
s_list = list(input())

k_index_start = -1
k_index_end = -1
k_before_index = -1
temp_katamari_count = 0
one_flag = False
index = 0

for s in s_list:
    if s == "0":
        one_flag = False
        if temp_katamari_count == k - 1 and k_before_index < 0:
            k_before_index = index - 1
        if temp_katamari_count == k and k_index_end < 0:
            k_index_end = index - 1
    else:
        if one_flag == False:
            temp_katamari_count = temp_katamari_count + 1
            one_flag = True
            if temp_katamari_count == k and k_index_start < 0:
                k_index_start = index
        if index == n - 1:
            if temp_katamari_count == k:
                k_index_end = index

    index = index + 1

result_list: List[str] = []
# 最初からk-1番目まで追加
result_list.extend(s_list[0 : k_before_index + 1])
# k番目の塊を移動
result_list.extend(s_list[k_index_start : k_index_end + 1])
# k-1番とK番目の間を追加
result_list.extend(s_list[k_before_index + 1 : k_index_start])
if k_index_end < n - 1:
    # 末尾を追加
    result_list.extend(s_list[k_index_end + 1 : n])

print("".join(result_list))
