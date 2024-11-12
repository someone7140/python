n, k = map(int, input().split())
s_list = list(input())

temp = 0
result = 0

for i in range(n):
    if s_list[i] == "O":
        temp = temp + 1
        if temp == k:
            result = result + 1
            temp = 0
    else:
        temp = 0

print(result)
