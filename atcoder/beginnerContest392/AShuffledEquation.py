a_list = list(map(int, input().split()))
a_list_sorted = sorted(a_list)

if a_list_sorted[0] * a_list_sorted[1] == a_list_sorted[2]:
    print("Yes")
else:
    print("No")
