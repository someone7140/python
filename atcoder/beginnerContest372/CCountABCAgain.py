from typing import List


n, q = map(int, input().split())
s = input()
s_list: List[str] = []
temp_result = 0
result_list: List[str] = []

for i in range(n):
    if i < n - 2:
        tempABC = s[i] + s[i + 1] + s[i + 2]
        if tempABC == "ABC":
            temp_result = temp_result + 1
    s_list.append(s[i])

for i in range(q):
    x_str, c = input().split()
    x = int(x_str) - 1
    if x < n - 2:
        tempABC = s_list[x] + s_list[x + 1] + s_list[x + 2]
        tempABC2 = c + s_list[x + 1] + s_list[x + 2]
        if tempABC == "ABC" and tempABC2 != "ABC":
            temp_result = temp_result - 1
        elif tempABC != "ABC" and tempABC2 == "ABC":
            temp_result = temp_result + 1
    if x < n - 1 and x > 0:
        tempABC = s_list[x - 1] + s_list[x] + s_list[x + 1]
        tempABC2 = s_list[x - 1] + c + s_list[x + 1]
        if tempABC == "ABC" and tempABC2 != "ABC":
            temp_result = temp_result - 1
        elif tempABC != "ABC" and tempABC2 == "ABC":
            temp_result = temp_result + 1
    if x > 1:
        tempABC = s_list[x - 2] + s_list[x - 1] + s_list[x]
        tempABC2 = s_list[x - 2] + s_list[x - 1] + c
        if tempABC == "ABC" and tempABC2 != "ABC":
            temp_result = temp_result - 1
        elif tempABC != "ABC" and tempABC2 == "ABC":
            temp_result = temp_result + 1
    result_list.append(str(temp_result))
    s_list[x] = c

print("\n".join(result_list))
