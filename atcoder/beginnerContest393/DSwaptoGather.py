n = int(input())
s_list = list(input())
s_list_reverse = s_list[::-1]

start_index = 0
end_index = 0
start_count = 1
end_count = 1
## まずはstartとendのindex
start_flag = False
for i in range(n):
    if s_list[i] == "1":
        start_index = i
        break
for i in range(n):
    if s_list_reverse[i] == "1":
        end_index = n - i - 1
        break

result = 0
while start_index < end_index:
    if start_count <= end_count:
        for i in range(start_index + 1, end_index + 1):
            if s_list[i] == "1":
                if i == start_index + 1:
                    start_count = start_count + 1
                    start_index = i
                    break
                else:
                    idou = i - start_index - 1
                    result = result + idou * start_count
                    start_count = start_count + 1
                    start_index = i
                    break
    else:
        for i in range(n - end_index, n - start_index + 1):
            if s_list_reverse[i] == "1":
                if i == n - end_index:
                    end_count = end_count + 1
                    end_index = n - i + 1
                    break
                else:
                    idou = i - (n - end_index)
                    result = result + idou * end_count
                    end_count = end_count + 1
                    end_index = n - i - 1
                    break

print(result)
