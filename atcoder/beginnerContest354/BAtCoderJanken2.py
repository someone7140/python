from dataclasses import dataclass
from typing import List

n = int(input())


@dataclass
class Sc:
    name: str
    rate: int

    def __lt__(self, other):
        return self.name < other.name


list_sc: List[Sc] = []
total = 0

for i in range(n):
    s, c_str = input().split()
    c = int(c_str)
    list_sc.append(Sc(s, c))
    total = total + c

sorted_sc_list = sorted(list_sc)
mod = total % n

print(sorted_sc_list[mod].name)
