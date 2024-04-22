from typing import Dict, List


n = int(input())
n_list = list(map(int, input().split()))

list_result: List[str] = []
n_dict: Dict[int, int] = {}
n_dict_by_value: Dict[int, int] = {}

for i in range(n):
    index = i + 1
    n_dict[index] = n_list[i]
    n_dict_by_value[n_list[i]] = index

for i in range(n):
    index = i + 1
    n_val = n_dict[index]
    if index != n_val:
        # 入れ替える
        index_2 = n_dict_by_value[index]

        n_dict[index] = index
        n_dict_by_value[index] = index

        n_dict[index_2] = n_val
        n_dict_by_value[n_val] = index_2

        list_result.append(str(index) + " " + str(index_2))

len_result = len(list_result)
if len_result == 0:
    print(0)
else:
    print(len_result)
    print("\n".join(list_result))
