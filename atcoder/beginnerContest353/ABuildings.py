n = int(input())
h_list = list(map(int, input().split()))

result = -1
first = h_list[0]
for i, h in enumerate(h_list):
    if i > 0 and first < h:
        result = i + 1
        break

print(result)
