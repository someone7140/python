from dataclasses import dataclass
from typing import List


n = int(input())


@dataclass
class Xy:
    num: int
    x: int
    y: int


list_xy: List[Xy] = []
list_result: List[str] = []

for i in range(n):
    x, y = map(int, input().split())
    list_xy.append(Xy(i + 1, x, y))

for xy1 in list_xy:
    saidai = -1
    num = 99999999999
    for xy2 in list_xy:
        temp = (xy1.x - xy2.x) * (xy1.x - xy2.x) + (xy1.y - xy2.y) * (xy1.y - xy2.y)
        if temp > saidai:
            saidai = temp
            num = xy2.num
    list_result.append(str(num))

print("\n".join(list_result))
