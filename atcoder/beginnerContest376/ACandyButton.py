n, c = map(int, input().split())
t_list = list(map(int, input().split()))

result = 0
before = 0

for i in range(n):
    if i == 0:
        result = result + 1
        before = t_list[i]
        continue

    sabun = t_list[i] - before
    if sabun >= c:
        result = result + 1
        before = t_list[i]

print(result)
