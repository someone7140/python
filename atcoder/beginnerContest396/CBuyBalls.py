from typing import List


n, m = map(int, input().split())
b_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

b_list_reverse = sorted(b_list, reverse=True)
w_list_reverse = sorted(w_list, reverse=True)

result = 0
temp = 0
white_plus_flag = True

for i in range(n):
    b = b_list_reverse[i]
    temp = temp + b
    if white_plus_flag and i <= (m - 1):
        w = w_list_reverse[i]
        if w <= 0:
            white_plus_flag = False
        else:
            temp = temp + w
    if temp > result:
        result = temp

print(result)
