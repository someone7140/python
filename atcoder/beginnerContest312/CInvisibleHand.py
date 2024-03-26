n, m = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_dict = {}
a_before = 0
a_list_sorted = sorted(a_list)
for a in a_list_sorted:
    if a in a_dict:
        a_dict[a] = a_dict[a] + 1
    else:
        a_dict[a] = 1 + a_before
    a_before = a_dict[a]

b_dict = {}
b_list_sorted = sorted(b_list, reverse=True)
b_before = 0
for b in b_list_sorted:
    if b in b_dict:
        b_dict[b] = b_dict[b] + 1
    else:
        b_dict[b] = 1 + b_before
    b_before = b_dict[b]

a_list_sorted = sorted(a_dict.keys())
b_list_sorted = sorted(b_dict.keys())
a_len = len(a_list_sorted)
b_len = len(b_list_sorted)

max_b = b_list_sorted[b_len - 1] + 1
max_a = a_list_sorted[b_len - 1] + 1
result = -1

a_index = 0
b_index = 0

while True:
    endFlag = a_index >= a_len - 1 and b_index >= b_len - 1

    a = a_list_sorted[a_index]
    b = b_list_sorted[b_index]

    if a <= b:
        a_count = a_dict[a]
        b_count = b_dict[b]
        if a_count >= b_count:
            if result >= a or result == -1:
                result = a
        if a_index < a_len - 1:
            a_index = a_index + 1
        else:
            b_index = b_index + 1
    else:
        if b_index < b_len - 1:
            b_index = b_index + 1
        else:
            a_index = a_index + 1

    if endFlag:
        break

if result == -1:
    result = max_b

print(result)
