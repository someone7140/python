from dataclasses import dataclass


n, m = map(int, input().split())


@dataclass
class Stone:
    x: int
    a: int


x_list = list(map(int, input().split()))
a_list = list(map(int, input().split()))
stone_list: list[Stone] = []

for i in range(m):
    stone_list.append(Stone(x_list[i], a_list[i]))

sorted_stone_list = sorted(stone_list, key=lambda x: x.x)

result = 0

tempPos = 1

for stone in sorted_stone_list:
    sabun = tempPos - stone.x
    if sabun < 0:
        result = -1
        break
    sabunPlus = stone.a * sabun
    tempPos = tempPos + stone.a
    result = result + stone.a * (stone.a - 1) // 2 + sabunPlus
    if tempPos > n + 1:
        result = -1
        break

print(result)
