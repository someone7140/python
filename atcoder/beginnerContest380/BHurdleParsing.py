from typing import List


s_list = list(input())

result_list: List[str] = []

temp_count = -1

for s in s_list:
    if s == "|":
        if temp_count > -1:
            result_list.append(str(temp_count))
        temp_count = 0
    else:
        temp_count = temp_count + 1

print(" ".join(result_list))
