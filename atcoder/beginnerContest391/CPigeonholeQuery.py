from typing import Dict, List, Set


n, q = map(int, input().split())
hato_su_dict: Dict[int, int] = {}
su_count_dict: Dict[int, int] = {}
su_several_id_set: Set[int] = set()


for i in range(n):
    hato_su_dict[i + 1] = i + 1
    su_count_dict[i + 1] = 1

result_list: List[str] = []

for i in range(q):
    q_str = input()
    if q_str == "2":
        result_list.append(str(len(su_several_id_set)))
    else:
        _, p, h = map(int, q_str.split())
        now_su = hato_su_dict[p]
        now_su_count = su_count_dict[now_su]
        now_next_su_count = su_count_dict[h]

        if now_su_count == 2:
            su_several_id_set.remove(now_su)
        if now_next_su_count == 1:
            su_several_id_set.add(h)
        hato_su_dict[p] = h
        su_count_dict[now_su] = su_count_dict[now_su] - 1
        su_count_dict[h] = su_count_dict[h] + 1

print("\n".join(result_list))
