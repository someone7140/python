from typing import List


n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_set = set(a_list)
results: List[str] = []

for i in range(1, n + 1):
    if i in a_set:
        continue
    else:
        results.append(str(i))

print(len(results))
print(" ".join(results))
