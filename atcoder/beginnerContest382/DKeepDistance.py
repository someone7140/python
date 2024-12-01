from typing import List


n, m = map(int, input().split())

result_list: List[str] = []


def saiki(now_val: int, temp_list: List[str], hitoketame: int):
    global m
    global result_list

    # 10足す
    now_val2 = now_val + 10
    if now_val2 > m:
        result_list.append(" ".join(temp_list))
    else:
        for i in range(0, n - hitoketame + 1):
            now_val3 = now_val2 + i
            if now_val3 <= m:
                temp_list.append(str(now_val3))
                saiki(now_val3, temp_list, hitoketame)
                temp_list.pop()


for i in range(n):
    temp_list: List[str] = [str(i + 1)]
    saiki(i + 1, temp_list, i + 1)

print("\n".join(result_list))
