from dataclasses import dataclass
from typing import List


n, d = map(int, input().split())


@dataclass
class SnakeClass:
    futosa: int
    nagasa: int


snake_list: List[SnakeClass] = []

for i in range(n):
    t, l = map(int, input().split())
    snake_list.append(SnakeClass(t, l))

result_list: List[str] = []
for i in range(1, d + 1):
    max = -1
    for snake in snake_list:
        temp = snake.futosa * (snake.nagasa + i)
        if temp > max:
            max = temp
    result_list.append(str(max))

print("\n".join(result_list))
