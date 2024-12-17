n, s = map(int, input().split())
a_list = list(map(int, input().split()))

amari = s % sum(a_list)

a_list_new = a_list + a_list


def hantei():
    global a_list_new
    global amari
    global n
    if amari == 0:
        print("Yes")
        return

    loop_flag = True
    start_index = 0
    end_index = 0

    result = "No"
    temp_sum = 0
    first_flag = True
    while loop_flag:
        if start_index == 2 * n - 2:
            loop_flag = False
            break
        if first_flag:
            temp_sum += a_list_new[end_index]
            first_flag = False
            continue
        if temp_sum == amari:
            result = "Yes"
            loop_flag = False
            break
        if temp_sum < amari:
            if end_index == 2 * n - 2:
                loop_flag = False
                break
            end_index = end_index + 1
            temp_sum += a_list_new[end_index]
            continue
        if temp_sum > amari:
            if end_index == start_index:
                temp_sum = a_list_new[end_index + 1]
                end_index = end_index + 1
                start_index = start_index + 1
            else:
                temp_sum = temp_sum - a_list_new[start_index]
                start_index = start_index + 1

    print(result)


hantei()
