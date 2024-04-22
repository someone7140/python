n, q = map(int, input().split())
t_list = map(int, input().split())

den_list = [True] * n

for i in t_list:
    index = i - 1
    if den_list[index]:
        den_list[index] = False
    else:
        den_list[index] = True

result = 0
for den in den_list:
    if den:
        result = result + 1

print(result)
