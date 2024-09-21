import bisect
from dataclasses import dataclass
from typing import Dict, List


n = int(input())
h_list = list(map(int, input().split()))
result_list: List[str] = []


@dataclass
class HInfo:
    h: int
    base_index: int
    sorted_index: int


h_dict: Dict[int, HInfo] = {}
for i in range(n):
    h_dict[h_list[i]] = HInfo(h_list[i], i, -1)
h_sorted_list = sorted(h_list)
for i in range(n):
    temp_h_info = h_dict[h_sorted_list[i]]
    h_dict[h_sorted_list[i]] = HInfo(h_sorted_list[i], temp_h_info.base_index, i)

sorted_len = n
delete_sorted_list: List[int] = []
for i in range(n):
    if i == n - 1:
        result_list.append("0")
        break
    sorted_index = h_dict[h_list[i]].sorted_index
    deleted_count = bisect.bisect_left(delete_sorted_list, sorted_index)
    temp_result = n - sorted_index - deleted_count
    result_list.append(str(temp_result))
    # 消す
    h_sorted_list.pop(sorted_index - deleted_count)
    h_dict.pop(h_list[i])
    bisect.insort_left(delete_sorted_list, sorted_index)

print("\n".join(result_list))
