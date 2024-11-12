from typing import List


n = int(input())

list_g: List[tuple] = []

for i in range(n):
    q, r = map(int, input().split())
    list_g.append((q, r))

result_list: List[str] = []
q = int(input())

for i in range(q):
    t, d = map(int, input().split())
    target_g = list_g[t - 1]
    amari = d % target_g[0]
    temp_result = d + (
        target_g[1] - amari
        if target_g[1] - amari >= 0
        else target_g[0] - amari + target_g[1]
    )
    result_list.append(str(temp_result))

print("\n".join(result_list))
