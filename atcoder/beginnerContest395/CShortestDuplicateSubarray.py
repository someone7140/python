from typing import List, Set

n = int(input())
a_list = list(map(int, input().split()))
a_set: Set[int] = set()
result = -1
result_list: List[int] = []
start_index = 0

for i in range(n):
    if i == 0:
        a_set.add(a_list[i])
    elif a_list[i] in a_set:
        temp_result = len(a_set) + 1
        if result == -1 or temp_result < result:
            result = temp_result
        # 重複がないところまで短くする
        for j in range(start_index, i):
            delete_target = a_list[j]
            if not a_list[i] in a_set:
                temp_result = len(a_set) + 2
                if result == -1 or temp_result < result:
                    result = temp_result
                start_index = j
                a_set.add(a_list[i])
                break
            elif len(a_set) == 1:
                temp_result = len(a_set) + 1
                start_index = j + 1
                if result == -1 or temp_result < result:
                    result = temp_result
                break

            else:
                a_set.remove(delete_target)
    else:
        a_set.add(a_list[i])

print(result)
