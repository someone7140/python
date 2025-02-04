from typing import List


n, m = map(int, input().split())

s_list_list: List[List[str]] = []
t_list_list: List[List[str]] = []
for i in range(n):
    s_list = list(input())
    s_list_list.append(s_list)
for i in range(m):
    t_list = list(input())
    t_list_list.append(t_list)

result = None

for i1 in range(n):
    for i2 in range(n):
        temp_result = True
        for k1 in range(m):
            for k2 in range(m):
                if k1 + i1 >= n or k2 + i2 >= n:
                    temp_result = False
                    break
                else:
                    if t_list_list[k1][k2] != s_list_list[k1 + i1][k2 + i2]:
                        temp_result = False
                        break
            if not temp_result:
                break
        if temp_result:
            result = str(i1 + 1) + " " + str(i2 + 1)
            break
    if result != None:
        break

print(result)
