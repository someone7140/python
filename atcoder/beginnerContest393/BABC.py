s_list = list(input())
s_len = len(s_list)
max_loop = s_len // 2 + 2

result = 0
index = 0
for s in s_list:
    if s == "A":
        for i in range(1, max_loop):
            second_index = index + i
            third_index = second_index + i
            if second_index >= s_len or third_index >= s_len:
                break
            else:
                if s_list[second_index] == "B" and s_list[third_index] == "C":
                    result = result + 1

    index = index + 1

print(result)
