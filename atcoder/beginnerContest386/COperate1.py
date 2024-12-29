n = int(input())

s_str = input()
t_str = input()
s_list = list(s_str)
t_list = list(t_str)
s_len = len(s_list)
t_len = len(t_list)

if s_len == t_len:
    index = 0
    sabun_count = 0
    while index < s_len:
        if s_list[index] != t_list[index]:
            sabun_count = sabun_count + 1
        index = index + 1
    if sabun_count < 2:
        print("Yes")
    else:
        print("No")
elif s_len - t_len == 1:
    index_s = 0
    index_t = 0
    sabun_count = 0
    while index_s < s_len:
        if s_list[index_s] != t_list[index_t]:
            sabun_count = sabun_count + 1
            if sabun_count > 1:
                break
            index_s = index_s + 1
        index_s = index_s + 1
        index_t = index_t + 1
        if index_t == t_len:
            break
    if sabun_count < 2:
        print("Yes")
    else:
        print("No")
elif t_len - s_len == 1:
    index_s = 0
    index_t = 0
    sabun_count = 0
    while index_t < t_len:
        if s_list[index_s] != t_list[index_t]:
            sabun_count = sabun_count + 1
            if sabun_count > 1:
                break
            index_t = index_t + 1
        index_s = index_s + 1
        index_t = index_t + 1
        if index_s == s_len:
            break
    if sabun_count < 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
