n = int(input())
result_list_list = [["" for j in range(n)] for i in range(n)]

for i in range(n):
    start_index = i
    bottom_index = n - 1 - i
    if start_index > bottom_index:
        break

    if i % 2 == 0:
        for j in range(start_index, bottom_index + 1):
            # 列の塗りつぶし
            result_list_list[start_index][j] = "#"
            result_list_list[bottom_index][j] = "#"
            # 行の塗りつぶし
            result_list_list[j][start_index] = "#"
            result_list_list[j][bottom_index] = "#"
    else:
        # 行の塗りつぶし
        for j in range(start_index, bottom_index + 1):
            # 列の塗りつぶし
            result_list_list[start_index][j] = "."
            result_list_list[bottom_index][j] = "."
            # 行の塗りつぶし
            result_list_list[j][start_index] = "."
            result_list_list[j][bottom_index] = "."

result = ""

for i in range(n):
    result += "".join(result_list_list[i])
    if i != n - 1:
        result += "\n"

print(result)
