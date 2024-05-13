from typing import List


n = int(input())


def parseFunc(str):
    if str == "100000000":
        return 0
    else:
        return int(str)


a_list = list(map(parseFunc, input().split()))
a_list_sorted = sorted(a_list)

ruisekiwa_list: List[int] = []
amari_list: List[int] = []
amari_ruisekiwa_list: List[int] = []
a_list_sorted2: List[int] = []

for i, a in enumerate(a_list_sorted):
    a_list_sorted2.append(a)
    if i == 0:
        ruisekiwa_list.append(a)
    else:
        ruisekiwa_list.append(a + ruisekiwa_list[i - 1])

    amari = a - 50000000
    amari_list.append(amari)
    if i == 0:
        amari_ruisekiwa_list.append(amari)
    else:
        amari_ruisekiwa_list.append(amari + amari_ruisekiwa_list[i - 1])

result = 0


def nibun(array_a_temp: List[int], x: int, now: int):
    global n

    start = 0
    end = n - now - 2
    half = (start + end) // 2

    while True:
        if start >= half or end < half:
            break

        if array_a_temp[half] + x < 100000000:
            start = half
            half = (start + end) // 2
        else:
            end = half
            half = (start + end) // 2

    return half


for i, a in enumerate(a_list_sorted):
    a_list_sorted2.pop(0)
    if i < n - 1:
        if a + a_list_sorted2[n - i - 2] < 100000000:
            ruiseki = ruisekiwa_list[n - 1] - ruisekiwa_list[i]
            result = result + ruiseki + a * (n - i - 1)
        elif a + a_list_sorted2[0] >= 100000000:
            amari_ruiseki = amari_ruisekiwa_list[n - 1] - amari_ruisekiwa_list[i]
            if a >= 50000000:
                result = result + amari_ruiseki + amari_list[i] * (n - i - 1)
            else:
                result = result + amari_ruiseki + a * (n - i - 1)
        else:
            index = nibun(a_list_sorted2, a, i)
            ruiseki = ruisekiwa_list[index] - ruisekiwa_list[i]
            result = result + ruiseki + a * (index + 1)
            amari_ruiseki = (
                amari_ruisekiwa_list[index + 1] - amari_ruisekiwa_list[index]
            )
            if a >= 50000000:
                result = result + amari_ruiseki + amari_list[i] * (n - i - index)
            else:
                result = result + amari_ruiseki + a * (n - i - index)

print(result)
