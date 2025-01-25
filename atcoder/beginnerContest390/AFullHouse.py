from typing import Dict


a_list = list(map(int, input().split()))
target_list = [1, 2, 3, 4, 5]
ng_list = []

for i in range(5):
    if a_list[i] != target_list[i]:
        ng_list.append(i)


if len(ng_list) != 2:
    print("No")
else:
    if ng_list[1] - ng_list[0] == 1:
        print("Yes")
    else:
        print("No")
