a_list = map(int, input().split())

one_count = 0
two_count = 0
three_count = 0
four_count = 0

for a in a_list:
    if a == 1:
        one_count = one_count + 1
    if a == 2:
        two_count = two_count + 1
    if a == 3:
        three_count = three_count + 1
    if a == 4:
        four_count = four_count + 1

print(one_count // 2 + two_count // 2 + three_count // 2 + four_count // 2)
