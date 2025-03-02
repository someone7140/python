from typing import List

n = int(input())
a_list = list(map(int, input().split()))

temp = -1
result = "Yes"
for i in range(n):
    if temp < a_list[i]:
        temp = a_list[i]
    else:
        result = "No"
        break

print(result)
