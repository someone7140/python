from dataclasses import dataclass
from typing import Dict, List

n = int(input())


@dataclass
class Ac:
    attack: str
    cost: int
    index: int
    key: str

    def __lt__(self, other):
        if self.attack < other.attack:
            return True
        else:
            if self.attack > other.attack:
                return False
            else:
                return self.cost < other.cost


list_ac: List[Ac] = []

for i in range(n):
    a, c = map(int, input().split())
    list_ac.append(Ac(a, c, i + 1, str(a) + "-" + str(c)))

sorted_ac_list: List[Ac] = sorted(list_ac)
delete_set = set()
ac_dict: Dict[str, List[Ac]] = {}
unique_ac_list: List[Ac] = []

for i in range(n):
    if i == n - 1:
        if sorted_ac_list[i].key != sorted_ac_list[i - 1].key:
            unique_ac_list.append(sorted_ac_list[i])
    else:
        if sorted_ac_list[i].key != sorted_ac_list[i + 1].key:
            unique_ac_list.append(sorted_ac_list[i])

unique_loop_len = len(unique_ac_list)
for i in range(unique_loop_len - 1):
    if (
        unique_ac_list[i].attack < unique_ac_list[i + 1].attack
        and unique_ac_list[i].cost > unique_ac_list[i + 1].cost
    ):
        delete_set.add(unique_ac_list[i].key)

result_list: List[int] = []
for i in range(n):
    if sorted_ac_list[i].key not in delete_set:
        result_list.append(sorted_ac_list[i].index)

result_list = sorted(result_list)


print(len(result_list))
print(" ".join([str(i) for i in result_list]))
