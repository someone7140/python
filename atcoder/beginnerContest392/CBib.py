from dataclasses import dataclass
from typing import Dict, List


n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))


@dataclass
class Human:
    id: int
    zekken: int
    mitsumeru_id: int

    def __lt__(self, other):
        return self.zekken < other.zekken


human_list: List[Human] = []
human_dict: Dict[int, Human] = {}

for i in range(1, n + 1):
    id = i
    zekken = q_list[i - 1]
    mitsumeru_id = p_list[i - 1]
    human = Human(id=id, zekken=zekken, mitsumeru_id=mitsumeru_id)
    human_list.append(human)
    human_dict[id] = human

results: List[str] = []
human_list_sorted = sorted(human_list, key=lambda x: x.zekken)
for human in human_list_sorted:
    mitsumeru_id = human.mitsumeru_id
    results.append(str(human_dict[mitsumeru_id].zekken))

print(" ".join(results))
