from typing import List

s = input()
s_swap = s.swapcase()
s_len = len(s)
q = int(input())
k_list = list(map(int, input().split()))
result_list: List[str] = []
max_index = 1000000000000000000
# フィボナッチ数列を列挙
a, b = 0, 1
fib_l = []
fib_rui = []
temp_index = 0

while temp_index <= 1000000000000000000:
    temp_index = b * s_len
    fib_l.append(temp_index)
    a, b = b, a + b

rui = 0
for fib in fib_l:
    rui = rui + fib
    fib_rui.append(rui)

len_fib_fib_rui = len(fib_rui)


def nibun_search(target_index: int):
    global fib_l

    start = 0
    end = len_fib_fib_rui - 1
    half = (start + end) // 2

    if fib_rui[0] >= target_index:
        return 0

    while True:
        if start >= half or end <= half:
            break

        if fib_rui[half] >= target_index:
            end = half
            half = (start + end) // 2
        else:
            start = half
            half = (start + end) // 2

    return half + 1


for k in k_list:
    target_index = nibun_search(k)
    if target_index == 0:
        result_list.append(str(s[k - 1]))
    else:
        fib = fib_l[target_index]
        target_index_2 = k - fib_rui[target_index - 1]
        syou = target_index_2 // s_len
        amari = target_index_2 % s_len
        if amari == 0:
            syou = syou - 1
            if syou % 2 == 0:
                result_list.append(str(s_swap[s_len - 1]))
            else:
                result_list.append(str(s[s_len - 1]))
        else:
            if syou % 2 == 0:
                result_list.append(str(s_swap[amari - 1]))
            else:
                result_list.append(str(s[amari - 1]))

print(" ".join(result_list))
