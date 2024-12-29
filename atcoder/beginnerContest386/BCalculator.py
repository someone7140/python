s_list = list(input())
s_len = len(s_list)

result = 0
index = 0
while index < s_len:
    s = s_list[index]
    if s == "0" and index < s_len - 1:
        s_next = s_list[index + 1]
        if s_next == "0":
            result = result + 1
            index = index + 2
        else:
            result = result + 1
            index = index + 1
    else:
        result = result + 1
        index = index + 1

print(result)
