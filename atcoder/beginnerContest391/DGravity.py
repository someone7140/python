import copy
from dataclasses import dataclass
from typing import Dict, List


n, w = map(int, input().split())


@dataclass
class DGravityBlock:
    id: int
    x: int
    y: int
    syoumetsu: int | None


block_list_list = [[None for j in range(w)] for i in range(n)]
visted_list_list = copy.deepcopy(block_list_list)
block_dict: Dict[int, DGravityBlock] = {}

for i in range(n):
    id = i + 1
    x, y = map(int, input().split())
    block = DGravityBlock(id=id, x=x - 1, y=y - 1, syoumetsu=None)
    block_list_list[y - 1][x - 1] = block
    block_dict[id] = block

now_second = 0
none_flag = False
for i1 in range(n):
    temp_second = now_second + 1
    temp_row_block: List[DGravityBlock] = []

    for i2 in range(w):
        temp_second2 = now_second + 1
        visited = visted_list_list[i1][i2]
        block = block_list_list[i1][i2] if not visited else None
        if visited or block == None:
            # 上に行く
            for i3 in range(i1 + 1, n):
                visited = visted_list_list[i3][i2]
                block = block_list_list[i3][i2] if not visited else None
                temp_second2 = temp_second2 + 1
                visted_list_list[i3][i2] = True
                if not visited and block != None:
                    temp_row_block.append(block)
                    break
            if block == None:
                none_flag = True
        else:
            temp_row_block.append(block)
        if temp_second2 > temp_second:
            temp_second = temp_second2
        visted_list_list[i1][i2] = True
    if none_flag:
        break
    else:
        now_second = temp_second
        for block in temp_row_block:
            new_block = DGravityBlock(
                id=block.id, x=block.x, y=block.y, syoumetsu=now_second
            )
            block_list_list[block.y][block.x] = new_block
            block_dict[new_block.id] = new_block

result_list: List[str] = []

q = int(input())
for i in range(q):
    t, id = map(int, input().split())
    block = block_dict[id]
    if block.syoumetsu == None or block.syoumetsu > t:
        result_list.append("Yes")
    else:
        result_list.append("No")


print("\n".join(result_list))
