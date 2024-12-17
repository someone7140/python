n, c1, c2 = input().split()
s_list = list(input())

result = ""
for s in s_list:
    if s != c1:
        result = result + c2
    else:
        result = result + c1

print(result)
