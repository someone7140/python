n = int(input())
a_list = list(map(int, input().split()))
syou: int | None = None

result = "Yes"
for i in range(n - 1):
    if syou == None:
        syou = a_list[i + 1] / a_list[i]
    else:
        if syou * a_list[i] != a_list[i + 1]:
            result = "No"
            break

print(result)
