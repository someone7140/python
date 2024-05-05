from typing import List


s = input()
t = input()

s_moji_list = list(s)
result_list: List[str] = []
pos = 0
for i, t_moji in enumerate(list(t)):
    if t_moji == s_moji_list[pos]:
        result_list.append(str(i + 1))
        pos = pos + 1


print(" ".join(result_list))
