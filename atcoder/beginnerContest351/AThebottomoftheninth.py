a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_sum = sum(a_list)
b_sum = sum(b_list)

result = a_sum - b_sum

if result < 0:
    result = 0
else:
    result = result + 1

print(result)
