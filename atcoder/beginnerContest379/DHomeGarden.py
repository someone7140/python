from dataclasses import dataclass
from typing import Dict, List


q = int(input())

ueki_list: List[int] = []
ueki_len = 0
day_ueki_max_index_dict: Dict[int, int] = {}

now_day = 0
result_list: List[str] = []

start_index = 0
for i in range(q):
    input_str = input()
    if input_str == "1":
        ueki_list.append(now_day)
        ueki_len = ueki_len + 1
        day_ueki_max_index_dict[now_day] = ueki_len - 1
    else:
        q, val_str = input_str.split()
        if q == "2":
            day = int(val_str)
            now_day = now_day + day
        if q == "3":
            target_h = int(val_str)
            temp_index = start_index
            loop_flag = True
            temp_result = 0
            while loop_flag:
                if temp_index >= ueki_len:
                    loop_flag = False
                else:
                    temp_day = ueki_list[temp_index]
                    h = now_day - temp_day
                    if h < target_h:
                        loop_flag = False
                    else:
                        max_index = day_ueki_max_index_dict[temp_day]
                        temp_result = temp_result + max_index - temp_index + 1
                        temp_index = max_index + 1
                        day_ueki_max_index_dict.pop(temp_day)
            result_list.append(str(temp_result))
            start_index = temp_index

print("\n".join(result_list))
