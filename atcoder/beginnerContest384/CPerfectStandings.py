import itertools
from typing import Dict, List


abcde_list = list(map(int, input().split()))
abcde_index_list: List[int] = [0, 1, 2, 3, 4]


def to_mojiretsu(index: int):
    if index == 0:
        return "A"
    if index == 1:
        return "B"
    if index == 2:
        return "C"
    if index == 3:
        return "D"
    if index == 4:
        return "E"
    return ""


tensuu_dict: Dict[int, List[str]] = {}

# 5個の場合はABCDE固定
tensuu_dict[sum(abcde_list)] = ["ABCDE"]

# 4個の場合
for comb in itertools.combinations(abcde_index_list, 4):
    sum = (
        abcde_list[comb[0]]
        + abcde_list[comb[1]]
        + abcde_list[comb[2]]
        + abcde_list[comb[3]]
    )
    name = (
        to_mojiretsu(comb[0])
        + to_mojiretsu(comb[1])
        + to_mojiretsu(comb[2])
        + to_mojiretsu(comb[3])
    )
    temp_list = tensuu_dict.get(sum)
    if temp_list == None:
        tensuu_dict[sum] = [name]
    else:
        tensuu_dict[sum].append(name)

# 3個の場合
for comb in itertools.combinations(abcde_index_list, 3):
    sum = abcde_list[comb[0]] + abcde_list[comb[1]] + abcde_list[comb[2]]
    name = to_mojiretsu(comb[0]) + to_mojiretsu(comb[1]) + to_mojiretsu(comb[2])
    temp_list = tensuu_dict.get(sum)
    if temp_list == None:
        tensuu_dict[sum] = [name]
    else:
        tensuu_dict[sum].append(name)

# 2個の場合
for comb in itertools.combinations(abcde_index_list, 2):
    sum = abcde_list[comb[0]] + abcde_list[comb[1]]
    name = to_mojiretsu(comb[0]) + to_mojiretsu(comb[1])
    temp_list = tensuu_dict.get(sum)
    if temp_list == None:
        tensuu_dict[sum] = [name]
    else:
        tensuu_dict[sum].append(name)

# 1個の場合
for comb in itertools.combinations(abcde_index_list, 1):
    sum = abcde_list[comb[0]]
    name = to_mojiretsu(comb[0])
    temp_list = tensuu_dict.get(sum)
    if temp_list == None:
        tensuu_dict[sum] = [name]
    else:
        tensuu_dict[sum].append(name)

result_list: List[str] = []
# 合計値を降順でソート
sum_keys = sorted(list(tensuu_dict.keys()), reverse=True)
for key in sum_keys:
    name_list = sorted(tensuu_dict[key])
    result_list = result_list + name_list

print("\n".join(result_list))
