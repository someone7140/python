n = int(input())

result = 0
time = 0
for i in range(n):
    t, v = map(int, input().split())
    time_sabun = t - time
    if time_sabun > result:
        result = 0
    else:
        result = result - time_sabun
    result = result + v
    time = t

print(result)
