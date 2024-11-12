from typing import Dict, List


n = int(input())
a_list = map(int, input().split())

h_dict: Dict[int, int] = {}
result_list: List[str] = []

index = 1
for a in a_list:
    result = h_dict.get(a, -1)
    result_list.append(str(result))
    h_dict[a] = index
    index = index + 1

print(" ".join(result_list))
