from typing import Dict, List

n, m = map(int, input().split())

result_list: List[str] = []
p_list = [0] * n
p_group_dict: Dict[int, int] = {}
p_group_reverse_dict: Dict[int, int] = {}

for i in range(n):
    p_list[i] = i
    p_group_dict[i] = i
    p_group_reverse_dict[i] = i

for i in range(m):
    input_strs = input().split()
    if input_strs[0] == "1":
        p_index = int(input_strs[1]) - 1
        move_group = int(input_strs[2]) - 1
        move_index = p_group_reverse_dict[move_group]
        p_list[p_index] = move_index
    elif input_strs[0] == "2":
        group_1 = int(input_strs[1]) - 1
        group_1_reverse = p_group_reverse_dict[group_1]
        group_2 = int(input_strs[2]) - 1
        group_2_reverse = p_group_reverse_dict[group_2]
        p_group_reverse_dict[group_1] = group_2_reverse
        p_group_reverse_dict[group_2] = group_1_reverse
        p_group_dict[group_1_reverse] = group_2
        p_group_dict[group_2_reverse] = group_1
    else:
        p_index = int(input_strs[1]) - 1
        p_group_index = p_list[p_index]
        result = p_group_dict[p_group_index] + 1
        result_list.append(str(result))

print("\n".join(result_list))
