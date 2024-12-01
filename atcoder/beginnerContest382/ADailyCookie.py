n, d = map(int, input().split())
s_list = list(input())

result = n

for s in s_list:
    if s == "@":
        result = result - 1

result = result + d

print(result)
