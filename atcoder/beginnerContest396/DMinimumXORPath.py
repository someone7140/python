from dataclasses import dataclass
import sys
from typing import Dict, List, Set


n, m = map(int, input().split())


@dataclass
class Ikisaki:
    pos: int
    w: int


ikisaki_dict: Dict[int, List[Ikisaki]] = {}
result = sys.maxsize

for i in range(m):
    v1, v2, w = map(int, input().split())
    # v1の登録
    v1_list = ikisaki_dict.get(v1)
    if v1_list == None:
        ikisaki_dict[v1] = [Ikisaki(v2, w)]
    else:
        ikisaki_dict[v1] = v1_list + [Ikisaki(v2, w)]
    # v2の登録
    v2_list = ikisaki_dict.get(v2)
    if v2_list == None:
        ikisaki_dict[v2] = [Ikisaki(v1, w)]
    else:
        ikisaki_dict[v2] = v2_list + [Ikisaki(v1, w)]

one_list = ikisaki_dict[1]


def loop_ikisaki(iki: Ikisaki, visited: set[int], temp: int | None):
    global ikisaki_dict
    global result
    global n

    temp = iki.w if temp == None else temp ^ iki.w
    if iki.pos == n:
        if temp < result:
            result = temp
    else:
        # 再起
        visited.add(iki.pos)
        next_list = ikisaki_dict.get(iki.pos)
        if next_list != None:
            for next in next_list:
                if not (next.pos in visited):
                    loop_ikisaki(next, visited, temp)
        visited.remove(iki.pos)


visited_set = set([1])
for one_ikisaki in one_list:
    loop_ikisaki(one_ikisaki, visited_set, None)

print(result)
