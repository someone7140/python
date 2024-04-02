from typing import List


n, a, b = map(int, input().split())
d_list = list(map(int, input().split()))

result = "No"

sabun_sum = 0
amari_list: List[int] = []

for d in d_list:
    amari = d % (a + b)
    amari_list.append(amari)

result = "Yes"
start = -1
end = -1

for d in d_list:
    # あまりの判定
    amari = d % (a + b)
    if amari > a:
        result = "No"
        break

    is_success = False
    if end == -1:
        end = a + b
        is_success = True
    else:
        if (d + end) % (a + b) > a:
            # endをより小さい値で更新
            update = (d + end) % (a + b) - a
            if update < start and update < end:
                result = "No"
                break
            else:
                end = update
        else:
            is_success = True

    if start == -1:
        start = a + b - d + 1
        is_success = True
    else:
        if (d + start) % (a + b) > a:
            # startをより大きい値で更新
            update = (d + start) % (a + b) - a
            if update > end and update > start:
                result = "No"
                break
            else:
                start = update
        else:
            is_success = True

    if is_success == False:
        result = "No"
        break

print(result)
