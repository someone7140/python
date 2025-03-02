from typing import Set

n, m = map(int, input().split())
uv_set: Set[str] = set()

result = 0
for i in range(m):
    u, v = map(int, input().split())
    if u == v:
        result = result + 1
    else:
        min = u if u < v else v
        max = v if u < v else u
        key = str(min) + "-" + str(max)
        if key in uv_set:
            result = result + 1
        else:
            uv_set.add(key)

print(result)
