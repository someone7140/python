n = int(input())
a_list = list(map(int, input().split()))
a_list_sorted = sorted(a_list)


def nibun(target_val: int, target_index: int):
    global a_list_sorted
    global n

    start = target_index
    end = n - 1
    half = (start + end) // 2

    while True:
        if start >= half or end <= half:
            break

        if target_val * 2 <= a_list_sorted[half]:
            end = half
            half = (start + end) // 2
        else:
            start = half
            half = (start + end) // 2

    return half


result = 0

max = a_list_sorted[n - 1]
for i in range(n - 1):
    if max >= a_list_sorted[i] * 2:
        nibun_index = nibun(a_list_sorted[i], i)
        if a_list_sorted[i] * 2 > a_list_sorted[nibun_index]:
            nibun_index = nibun_index + 1
            result = result + (n - nibun_index)
        else:
            result = result + (n - nibun_index)

print(result)
