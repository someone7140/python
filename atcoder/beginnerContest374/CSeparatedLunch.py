import sys


n = int(input())
k_list = list(map(int, input().split()))

list_1_sum = 0
list_2_sum = 0

result = sys.maxsize


def saiki_group(index: int):
    global result
    global k_list
    global list_1_sum
    global list_2_sum
    global n

    if index == n:
        temp_result = list_1_sum if list_1_sum > list_2_sum else list_2_sum
        if temp_result < result:
            result = temp_result

    else:
        # list_1に足す
        list_1_sum = list_1_sum + k_list[index]
        saiki_group(index + 1)
        # 戻す
        list_1_sum = list_1_sum - k_list[index]

        # list_2に足す
        list_2_sum = list_2_sum + k_list[index]
        saiki_group(index + 1)
        # 戻す
        list_2_sum = list_2_sum - k_list[index]


saiki_group(0)

print(result)
