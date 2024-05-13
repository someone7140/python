n, k = map(int, input().split())
a_list = list(map(int, input().split()))

count = 1
temp_count = 0

for a in a_list:
    if temp_count + a <= k:
        temp_count = temp_count + a
    else:
        temp_count = a
        count = count + 1

print(count)
