from typing import List


m = int(input())
three_list: List[int] = [1]
for i in range(10):
    temp3 = three_list[i] * 3
    three_list.append(temp3)

temp_m = m
result_list: List[int] = []

while temp_m > 0:
    for i in range(10, -1, -1):
        if temp_m >= three_list[i]:
            result_list.append(i)
            temp_m = temp_m - three_list[i]
            break

print(len(result_list))
print(" ".join([str(i) for i in result_list]))
