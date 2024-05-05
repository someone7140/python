from dataclasses import dataclass
from typing import List


n = int(input())

sum = 0
result = 0


@dataclass
class Ab:
    a: int
    b: int


ab_list: List[Ab] = []

for i in range(n):
    a, b = map(int, input().split())
    ab_list.append(Ab(a, b))
    sum = sum + a

for ab in ab_list:
    temp_result = sum - ab.a + ab.b
    if temp_result > result:
        result = temp_result

print(result)
