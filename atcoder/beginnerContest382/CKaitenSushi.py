from typing import Dict, List


n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

result_list: List[str] = []
a_value_index_dict: Dict[int, int] = {}
a_sorted_deleted: List[int] = []
a_sorted_deleted_len = 0

# 値とキーを紐づけるdictに入れていく
index = 1
for a in a_list:
    get_index = a_value_index_dict.get(a, None)
    if get_index == None:
        a_value_index_dict[a] = index

    if a_sorted_deleted_len == 0:
        a_sorted_deleted_len = a_sorted_deleted_len + 1
        a_sorted_deleted.append(a)
    else:
        before = a_sorted_deleted[a_sorted_deleted_len - 1]
        if before > a:
            a_sorted_deleted.append(a)
            a_sorted_deleted_len = a_sorted_deleted_len + 1

    index = index + 1


def nibun_search(target_val: int):
    global a_sorted_deleted
    global a_sorted_deleted_len

    start = 0
    end = a_sorted_deleted_len - 1
    half = (start + end) // 2

    while True:
        if start >= half or end <= half:
            break

        if a_sorted_deleted[half] <= target_val:
            end = half
            half = (start + end) // 2
        else:
            start = half
            half = (start + end) // 2

    return half


for b in b_list:
    if a_sorted_deleted[a_sorted_deleted_len - 1] > b:
        result_list.append("-1")
    else:
        target_index = nibun_search(b)
        if target_index < a_sorted_deleted_len - 1:
            if a_sorted_deleted[target_index] > b:
                result_list.append(
                    str(a_value_index_dict[a_sorted_deleted[target_index + 1]])
                )
            else:
                result_list.append(
                    str(a_value_index_dict[a_sorted_deleted[target_index]])
                )
        else:
            result_list.append(str(a_value_index_dict[a_sorted_deleted[target_index]]))

print("\n".join(result_list))
