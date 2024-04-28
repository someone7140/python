from typing import List


n = int(input())
a_list: List[str] = []

for i in range(n):
    a_list.append(input())

result_i = 0
result_j = 0

for i in range(n):
    b = input()
    a_word_list = list(a_list[i])
    b_word_list = list(b)
    if result_i > 0:
        pass
    else:
        for j in range(n):
            if a_word_list[j] != b_word_list[j]:
                result_i = i + 1
                result_j = j + 1
                break

print(str(result_i) + " " + str(result_j))
