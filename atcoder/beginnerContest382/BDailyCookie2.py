n, d = map(int, input().split())
s_list = list(input())
s_list.reverse()

result = ""
nokori_day = d

for s in s_list:
    if s == "@":
        if nokori_day <= 0:
            result = s + result
        else:
            result = "." + result
            nokori_day = nokori_day - 1
    else:
        result = "." + result

print(result)
