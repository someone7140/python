import math


n = int(input())

result = 0
now_x = 0
now_y = 0

for i in range(n):
    x, y = map(int, input().split())
    result = result + math.sqrt((now_x - x) * (now_x - x) + (now_y - y) * (now_y - y))
    now_x = x
    now_y = y

result = result + math.sqrt(now_x * now_x + now_y * now_y)
print(result)
